

import json

import boto3
import os

import time
time.sleep(10)

sqs_client = boto3.client("sqs")
QUEUE_URL = os.getenv("QUEUE_URL")
def lambda_handler(event, context):

    data = json.loads(event['body'])
    body =data['body']
    header=data['header']
    message={
        "header":header,
        "body":body
    }

    response = sqs_client.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response["MessageId"]
            # "location": ip.text.replace("\n", "")
        }),
    }


    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "hello world",
    #         # "location": ip.text.replace("\n", "")
    #         "data":"success"
    #     }),
    # }
