import pyrebase
import requests
from PIL import Image
from io import BytesIO

# Initialize firebase app
config = {
    "apiKey": "AIzaSyCbcpY3DVVKlUHDWW6BJHHyC_0tzUOmmRQ",
    "authDomain": "babble-98541.firebaseapp.com",
    "databaseURL": "https://babble-98541.firebaseio.com",
    "projectId": "babble-98541",
    "storageBucket": "babble-98541.appspot.com",
    "messagingSenderId": "454487413592",
    "appId": "1:454487413592:web:b27b00ffc37289ba064b2d",
    "measurementId": "G-GK5WMPJZDT"
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Download
# storage.child(firebase에 있는 파일 경로).download(파일 저장 이름)
url = storage.child('babble_15/초코.jpg').get_url(None)

res = requests.get(url)

img = Image.open(BytesIO(res.content))

img.show()