import os,json

# SQS キューの URL
sqs_queue_url = os.environ['SQS_QUEUE_URL']

def lambda_handler(event, context):

    print("event =", event)

    print("context =", context)
    
    # 受信した SQS イベントを処理
    for record in event['Records']:

        # SQS メッセージ情報を取得
        message = record['body']

        print("message = ", message)
    
    return {
        'statusCode': 200,
        'body': 'Messages processed successfully!'
    }
