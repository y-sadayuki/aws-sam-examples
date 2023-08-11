import json
import boto3
import os
import random
from boto3.dynamodb.conditions import Key
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DynamDbTestTable']


#ランダムで5分の区間を返す
def random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_date_start = start_date + timedelta(days=random_days)
    random_date_end = random_date_start + timedelta(minutes=5)
    return [random_date_start.strftime("%Y-%m-%d %H:%M:%S"),random_date_end.strftime("%Y-%m-%d %H:%M:%S")]

def query():
    
    print("Start AiInput: dynamoDB=",table_name)
    
    # DynamoDBへの接続準備
    dynamodb = boto3.resource('dynamodb')
    dynamodb_table = dynamodb.Table(table_name)
    
    #開始位置を取得
    start = "2023-01-01 00:00:00"
    end = "2023-01-01 00:00:00"
    
    #取得する区間を決定
    date_format = "%Y-%m-%d %H:%M:%S"
    start_time = datetime.strptime(start, date_format)
    end_time = datetime.strptime(end, date_format)
    between_time = random_date(start_time,end_time)
    print("between_time=",between_time)
    
    #50人からランダムで1人
    random_id = random.randint(0, 49)
    id = 'user-'  + str(random_id).zfill(5)
    print("select user_id=",id)
    
    print("query in")
    response = dynamodb_table.query(
        KeyConditionExpression=Key('id').eq(id) & Key('timestamp').between(between_time[0], between_time[1])
    )
    
    print("type=",type(response))
    
    # for文で辞書のキーと値をダンプして表示
    for key, value in response.items():
        print(f"Key: {key}, Value: {value}")
   
    print(response["Items"]) 
   
    for value in response["Items"]:
        print(value)
    
    print("query out")
    
    #print("res=",response["items"])
    print("res=",response)
    msg = "tablename="+table_name
    
    print("DynamoDB Table=",table_name)
    
    return {
        'statusCode': 200,
        'body': msg
    }

    