import requests
import json

url = "https://gv0ba0lqh3.execute-api.us-west-2.amazonaws.com/PROD/sklearn-on-aws-resource"

payload = json.dumps({
        "sepal length": 5.7,
        "sepal width": 2.9,
        "petal length": 4.2,
        "petal width": 1.3
        })

response = requests.request("POST", url, data=payload)
print(response.text)