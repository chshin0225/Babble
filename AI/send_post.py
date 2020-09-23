import requests
import json

def send_post():
    params = {
        "path": "babble_15/초코.jpg",
    }
    res = requests.post("http://127.0.0.1:5000/tags", data=json.dumps(params))
    return res.text

print(send_post())