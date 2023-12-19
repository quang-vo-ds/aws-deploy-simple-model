import requests
import json

headers = {'Content-Type': 'application/json'}
data = {"data":"you are beautiful!"}

print(requests.post("https://uots7e7rf2.execute-api.us-west-2.amazonaws.com/dev/prediction",
    headers=headers, data=json.dumps(data)))