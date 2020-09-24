from flask import Flask, request
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

app = Flask(__name__)
app.yolo = YOLO()
app.config['JSON_AS_ASCII'] = False

graph = tf.get_default_graph()

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
    with graph.as_default():
        tags += app.yolo.extract_tag(img)
        tags += GE.get_tag_emotion(img_emtion)  # add tags
        
    
    data = {
        'tags': tags
    }

    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')