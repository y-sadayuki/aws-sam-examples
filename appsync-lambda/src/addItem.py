import json
import os
import random
from datetime import datetime, timedelta

def lambda_handler(event, context):

    print("event=", event)  
    print("context=", context)  

    # クエリの引数から ID を取得
    #item_id = event["id"]

    # ID に基づいてデータを取得（この部分は適切な処理を行う必要があります）
    response = {
        "id": "1234",
    }

    print(response)

    return response

