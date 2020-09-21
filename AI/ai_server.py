from flask import Flask
# import 추가

app = Flask(__name__)

@app.route('/')
def index_page():
    return "AI Server!"

@app.route('/tags/<imgpath>')
def tags(imgpath):
    
    # image load
    img = 


    # get_tags_emotion(img) 함수 만들기
    tags = []
    tags += get_tags_emotion(img)
    tags += get_tags_objDetection(img)

    data = {
        'tags': tags
    }

    return data