from flask import Flask
import get_emotion
from PIL import Image
import requests
from io import BytesIO
import cv2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tags/<imgpath>')
def get_emotion_list(imgpath):
    print("imgpath : " + imgpath)
    #response = requests.get(imgpath)
    #img = Image.open(BytesIO(response.content))
    #img = cv2.imread(imgpath)
    e_list = get_emotion.get_tag_emotion(imgpath, 700, 700)
    res = ', '.join(e_list)
    return 'tags : ' + res

if __name__ == '__main__':
    app.run()