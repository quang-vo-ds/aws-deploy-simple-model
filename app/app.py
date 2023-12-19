import json
from transformers import pipeline

model_id = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
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
        'headers': {"Content-Type":"application/json"},
        'body': json.dumps(prediction),
        'isBase64Encoded': False
    }