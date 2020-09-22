from flask import Flask
from ObjDetection.yolo import YOLO
from PIL import Image
import tensorflow as tf
# import 추가

app = Flask(__name__)
app.yolo = YOLO()
app.config['JSON_AS_ASCII'] = False

graph = tf.get_default_graph()
@app.route('/')
def index_page():
    return "AI Server!"

@app.route('/tags/<imgpath>')
def tags(imgpath):
    
    # image load
    # 일달 임시적으로 로컬에 있는 이미지 로드하는 걸루 해놨음 
    img = Image.open('./ObjDetection/example.JPG')


    tags=[] # 추출된 tag가 담길 list

    # obj detection을 통한 tag 추출
    with graph.as_default():
        tags += app.yolo.extract_tag(img)


    data = {
        'tags': tags
    }

    return data

if __name__ == '__main__':
    app.run()