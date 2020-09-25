from flask import Flask, request
from Emotion import get_emotion as GE
from PIL import Image
from io import BytesIO
import json
import requests
import pickle
import tensorflow as tf
import cv2
import time
from keras import backend as KB

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index_page():
    return "AI Server!"

@app.route('/emotion', methods=['POST'])
def emotion():
    start = time.time()
    path = json.loads(request.get_data(), encoding='utf-8')          
    url = path['path']
    print(url)
    # url to img
    img_emtion = GE.url_to_image(url) 
    
    cv2.imshow("test", img_emtion)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    tag = []
    
    
    tag = GE.get_tag_emotion(img_emtion)        
    
    print(tag)
    print("time :", time.time() - start)
    return ""

if __name__ == '__main__':
    app.run()