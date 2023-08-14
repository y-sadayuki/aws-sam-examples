import json
import os
import boto3

def lambda_handler(event, context):

    sqs_queue_url = os.environ['SQS_QUEUE_URL']

    # SQS キューに送信するメッセージ
    message_body = 'Hello, SQS from Lambda!'
    
    # Boto3 クライアントを作成
    sqs_client = boto3.client('sqs')

    print("sqs message:",sqs_queue_url)
    
    # メッセージを SQS キューに送信
    response = sqs_client.send_message(
        QueueUrl=sqs_queue_url,
        MessageBody=message_body
    )

    print(response)
    
    return {
        'statusCode': 200,
        'body': 'Message sent to SQS successfully!'
    }