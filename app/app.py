import json
from transformers import pipeline

model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
classifier = pipeline("sentiment-analysis", model=model_id)

def handler(event, context):
    # we expect a "data" key in the "body" of our event.
    data = json.loads(event["body"])["data"]
    print(f"making a prediction on the text: {data}")
    # make prediction
    prediction = classifier(data)
    print(f"prediction: {prediction}")
    return {
        'statusCode': 200,
        'body': json.dumps(prediction)
    }

if __name__ == "__main__":
    # import torch
    # import transformers
    # print(torch.__version__)
    # print(transformers.__version__)
    print(classifier("The restaurant is really bad!"))