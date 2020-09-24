from flask import Flask, request
from flask_cors import CORS
from ObjDetection.yolo import YOLO
from Emotion import get_emotion as GE
from PIL import Image
from io import BytesIO
import json
import pyrebase
import requests
import pickle
import tensorflow as tf
import cv2
from keras import backend as KB

app = Flask(__name__)
app.yolo = YOLO()
app.config['JSON_AS_ASCII'] = False
CORS(app)


graph = tf.get_default_graph()

# Initialize firebase app
with open("config.pickle", "rb") as f:
    config = pickle.load(f)

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

@app.route('/')
def index_page():
    return "AI Server!"

@app.route('/emotion', methods=['POST'])
def emotion():
    path = json.loads(request.get_data(), encoding='utf-8')          
    path = path['path']
    url = storage.child(path).get_url(None)

    print(url)
    # url to img
    img_emtion = GE.url_to_image(url) 
    
    cv2.imshow("test", img_emtion)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    tag = []
    
    KB.clear_session()
    tag = GE.get_tag_emotion(img_emtion)        
    KB.clear_session()
    print(tag)
    return "asdf"

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
    with graph.as_default():
        tags += app.yolo.extract_tag(img)
    
    with graph.as_default():
        tags += GE.get_tag_emotion(img_emtion)  # add tags
        
    
    data = {
        'tags': tags
    }

    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')