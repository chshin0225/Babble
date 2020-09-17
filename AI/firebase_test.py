import pyrebase

# Initialize firebase app
config = {
    "apiKey": "AIzaSyBdMcBm_CrI9gGx0F-kjU6Q-Rxah0Q99z0",
    "authDomain": "babble-20baf.firebaseapp.com",
    "databaseURL": "https://babble-20baf.firebaseio.com",
    "projectId": "babble-20baf",
    "storageBucket": "babble-20baf.appspot.com",
    "messagingSenderId": "29022455607",
    "appId": "1:29022455607:web:5fffe19e5c4cff42af7cb2",
    "measurementId": "G-FQ6ZNW45P8"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Download
# storage.child(firebase에 있는 파일 경로).download(파일 저장 이름)
storage.child('playtime.jpg').download('playtime.jpg')

