from flask import Flask, request
from flask_cors import CORS
from ObjDetection.yolo import YOLO
from Emotion import get_emotion as GE
from deepface.extendedmodels import Emotion
from PIL import Image
from io import BytesIO
import json
import requests
import pickle
import tensorflow as tf
import cv2
from keras import backend as KB
import sys 
import pyrebase
from mtcnn import MTCNN
import time

app = Flask(__name__)
app.yolo = YOLO()
app.config['JSON_AS_ASCII'] = False
CORS(app)


graph = tf.get_default_graph()

mtcnn_detector = MTCNN()
detector = cv2.dnn.readNetFromCaffe("emotion\\files\\deploy.prototxt", "emotion\\files\\res10_300x300_ssd_iter_140000.caffemodel")
emotion_model = Emotion.loadModel()

# Initialize firebase app
with open("config.pickle", "rb") as f:
    config = pickle.load(f)

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

@app.route('/')
def index_page():
    return "AI Server!"

@app.route('/tags', methods=['POST'])
def tags():
    # firebase image path
    path = json.loads(request.get_data(), encoding='utf-8')
    path = path['path']

    # load image
    url = storage.child(path).get_url(None)    
    res = requests.get(url)
    img = Image.open(BytesIO(res.content))
    
    # url to img
    img_emtion = GE.url_to_image(url) 

    tags=[] # 추출된 tag가 담길 list

    # obj detection을 통한 tag 추출    
    start = time.time()
    with graph.as_default():
        tags += app.yolo.extract_tag(img)
    print(time.time() - start)
    start = time.time()
    with graph.as_default():
        tag_temp = GE.get_tag_emotion(img_emtion)
        if tag_temp == []:
            tag_temp = GE.get_tag_emotion(img_emtion, 500, 500)
            if tag_temp == []:
                tag_temp = GE.get_tag_emotion(img_emtion, 700, 700)
                
        tags += tag_temp  # add tags
    print(time.time() - start)
    data = {
        'tags': tags
    }

    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')