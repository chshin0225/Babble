import cv2
import pandas as pd
import time
import matplotlib.pylab as plt
import numpy as np
import math
import urllib.request
from PIL import Image
from pathlib import Path
from deepface import DeepFace
from deepface.commons import distance
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ai_server import mtcnn_detector, detector, emotion_model


def alignment_procedure(img, left_eye, right_eye):  # find degree and rotate image
    # this function aligns given face in img based on left and right eye coordinates
    left_eye_x, left_eye_y = left_eye
    right_eye_x, right_eye_y = right_eye

    # find rotation direction
    if left_eye_y > right_eye_y:
        point_3rd = (right_eye_x, left_eye_y)
        direction = -1  # rotate same direction to clock
    else:
        point_3rd = (left_eye_x, right_eye_y)
        direction = 1  # rotate inverse direction of clock
    
    # find length of triangle edges
    a = distance.findEuclideanDistance(np.array(left_eye), np.array(point_3rd))
    b = distance.findEuclideanDistance(
        np.array(right_eye), np.array(point_3rd))
    c = distance.findEuclideanDistance(np.array(right_eye), np.array(left_eye))    
    # apply cosine rule

    if b != 0 and c != 0:  # this multiplication causes division by zero in cos_a calculation
        cos_a = (b*b + c*c - a*a)/(2*b*c)
        angle = np.arccos(cos_a)  # angle in radian
        angle = (angle * 180) / math.pi  # radian to degree
        
        # rotate base image
        if direction == -1:
            angle = 90 - angle

        img = Image.fromarray(img)
        img = np.array(img.rotate(direction * angle))
    
    return img  # return img anyway


def align_face(img):  # rotate face to horizontal            
    detections = mtcnn_detector.detect_faces(img)
    
    if len(detections) > 0:
        detection = detections[0]
        keypoints = detection["keypoints"]
        left_eye = keypoints["left_eye"]
        right_eye = keypoints["right_eye"]

        img = alignment_procedure(img, left_eye, right_eye)
    
    return img  # return img anyway


def get_tag_emotion(image_file, tx=300, ty=300):  # return tag list      
    base_img = image_file.copy()  # back up original image
    original_size = base_img.shape

    # The higher the number, the easier it is to find a small face.
    target_size = (ty, tx)
    image_file = cv2.resize(image_file, target_size)
    aspect_ratio_x = (original_size[1] / target_size[1])
    aspect_ratio_y = (original_size[0] / target_size[0])

    # detector expects (1, 3, 300, 300) shaped input    
    imageBlob = cv2.dnn.blobFromImage(image=image_file)
    
    # imageBlob = np.expand_dims(np.rollaxis(image, 2, 0), axis = 0)
    detector.setInput(imageBlob)
    detections = detector.forward()

    column_labels = ["img_id", "is_face", "confidence", "left", "top", "right", "bottom"]
    detections_df = pd.DataFrame(detections[0][0], columns=column_labels)

    # 0: background, 1: face, confidence 가 높은게 얼굴일 확률이 높다
    detections_df = detections_df[detections_df['is_face'] == 1]
    detections_df = detections_df[detections_df['confidence'] > 0.90]

    detections_df['left'] = (detections_df['left'] * tx).astype(int)  # 좌표값을 정수형 데이터로 변환
    detections_df['bottom'] = (detections_df['bottom'] * ty).astype(int)
    detections_df['right'] = (detections_df['right'] * tx).astype(int)
    detections_df['top'] = (detections_df['top'] * ty).astype(int)

    detections_df = detections_df[detections_df['right'] < original_size[1]]
    detections_df = detections_df[detections_df['bottom'] < original_size[0]]

    face_list_df = pd.DataFrame(
        columns=['left', 'top', 'right', 'bottom'])  # pos of faces
    
    for i, instance in detections_df.iterrows():  # set face pos
        confidence_score = str(round(100*instance["confidence"], 2))+" %"
        left = instance["left"]
        right = instance["right"]
        bottom = instance["bottom"]
        top = instance["top"]

        face_list_df = face_list_df.append(
            {'left': left, 'top': top, 'right': right, 'bottom': bottom}, ignore_index=True)
    
    face_list_df = face_list_df.astype(int)
    # time to get face : 20ms    
    
    emotion_res_list = []  # return emotion each face
    emotion_labels = ['화남', '역겹', '무섭', '행복', '슬픔', '놀람', '무']    
    # emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

    for i, instance in face_list_df.iterrows():  # each face
        detected_face = base_img[int(instance['top'] * aspect_ratio_y):int(instance['bottom'] * aspect_ratio_y),
                                 int(instance['left'] * aspect_ratio_x):int(instance['right'] * aspect_ratio_x)]  # get face
        
        detected_face = align_face(detected_face)  # face rotate to horizontal, time to align : 60ms
        detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)  # to grey
        face48 = cv2.resize(detected_face, (48, 48))
        
        # normalization
        img_pixels = np.asarray(face48, 'float32')
        img_pixels = img_pixels.reshape(
            (img_pixels.shape[0], img_pixels.shape[1], 1))
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255  # normalize input in [0, 1]
        

        # get strongest emotions                      
        emotion_predictions = emotion_model.predict(img_pixels)[0, :]  # get emotion info use emotion model
        sum_of_predictions = emotion_predictions.sum()
        
        # get max emotion
        emotion_res = [emotion_labels[0], 100 * emotion_predictions[0] / sum_of_predictions]
        
        for i in range(1, len(emotion_labels)):
            emotion_prediction = 100 * emotion_predictions[i] / sum_of_predictions

            if(emotion_res[1] < emotion_prediction):
                emotion_res = [emotion_labels[i], emotion_prediction]

        if emotion_res[0] != "무":
            flag = 0
            for em in emotion_res_list:
                if em == emotion_res[0]:
                    flag = 1
            if flag == 0:
                emotion_res_list.append(emotion_res[0])    
        
    '''
    for i, instance in face_list_df.iterrows():  # draw rectangle and text
        cv2.putText(base_img, emotion_res_list[i], (int(instance['left']*aspect_ratio_x), int(instance['top']*aspect_ratio_y-10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
        cv2.rectangle(base_img, (int(instance['left'] * aspect_ratio_x), int(instance['top'] * aspect_ratio_y)),
                      (int(instance['right'] * aspect_ratio_x), int(instance['bottom'] * aspect_ratio_y)), (255, 255, 255), 3)
    
    imS = cv2.resize(base_img, (800, 800))
    cv2.imshow("test", imS)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    '''
    return emotion_res_list


def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format    
    resp = urllib.request.urlopen(url)    
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)	
    return image 
