import requests
import json
import time

def send_post():
    start = time.time()
    params = {
        "path": "babble_2/독서독서.jpg",
    }
    res = requests.post("http://127.0.0.1:5000/tags", data=json.dumps(params))
    print("time to return : " + str(time.time() - start))
    return res.text

print(send_post())