import pyrebase
import requests
import pickle
from PIL import Image
from io import BytesIO

# Initialize firebase app

with open("config.pickle", "rb") as f:
    config = pickle.load(f)

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Download
# storage.child(firebase에 있는 파일 경로).download(파일 저장 이름)
url = storage.child('babble_15/초코.jpg').get_url(None)


res = requests.get(url)

img = Image.open(BytesIO(res.content))

img.show()