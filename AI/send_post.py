import requests
import json

def send_post():
    params = {
        "path": "babble_2/독서독서.jpg",
    }
    res = requests.post("http://127.0.0.1:5000/emotion", data=json.dumps(params))
    return res.text

print(send_post())