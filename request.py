import requests
import json

url = "https://gv0ba0lqh3.execute-api.us-west-2.amazonaws.com/PROD/sklearn-on-aws-resource"

payload = json.dumps({"data": "5.7 2.9 4.2 1.3"})

response = requests.request("POST", url, data=payload)
print(response.text)