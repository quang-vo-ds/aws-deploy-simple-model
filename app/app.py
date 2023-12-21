import json
import os
import numpy as np
from joblib import load

model_file_name = 'svm.dump'
model_path = os.path.join("model", model_file_name)
model = load(model_path)
label_dict = {
    0: 'setosa', 
    1: 'versicolor', 
    2: 'virginica'
}

def lambda_handler(event, context):
    data = json.loads(json.dumps(event))
    payload = np.array([float(i) for i in data["data"].split()]).reshape(1,-1)
    y_pred = int(model.predict(payload)[0])
    prediction = label_dict[y_pred]

    return {
        'statusCode': 200,
        'body': prediction
    }

if __name__ == '__main__':
    event = {"data": "5.7 2.9 4.2 1.3"}
    print(lambda_handler(event, ""))
    # x = np.array([5.7,2.9,4.2,1.3]).reshape(1,-1)
    # print(label_dict[int(model.predict(x)[0])])