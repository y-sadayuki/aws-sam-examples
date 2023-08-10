import json
import boto3
import os
import csv
import io
import zipfile

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TEST_TABLE_NAME']
s3_name = os.environ['TEST_S3'] 
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    
    print("Start AiInput: dynamoDB=",table_name)
    
    s3_client = boto3.client('s3')
    bucket = 'test-bucket'
    key = 'dynamoDummyData.csv'
    response = s3_client.get_object(Bucket=bucket, Key=key)
    csv_data = response['Body'].read().decode('utf-8')
    
    csv_reader = csv.DictReader(csv_data.splitlines())
    data_list = []
    for row in csv_reader:
        data_list.append(row)
        
    print("datalen=",len(data_list))
    
    # DynamoDBへのデータ挿入
    dynamodb = boto3.resource('dynamodb')
    dynamodb_table = dynamodb.Table(table_name)
    
    #print(data_list[0:10])
    
     # データリストをバッチで書き込み
    for idx in range(0,len(data_list),25):
        batch_list = data_list[idx:idx+25]
        with dynamodb_table.batch_writer() as batch:
            print("idx=",idx)
            for item in batch_list:
                batch.put_item(Item=item)
    
    msg = "tablename="+table_name
    
    print("DynamoDB Table=",table_name)
    
    return {
        'statusCode': 200,
        'body': msg
    }

    
