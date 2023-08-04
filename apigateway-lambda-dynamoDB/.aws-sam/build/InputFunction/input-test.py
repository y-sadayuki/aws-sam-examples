import json
import os
import random
from datetime import datetime, timedelta

    
def lambda_handler(event, context):

    print("hello world")
    
    return {
        'statusCode': 200,
        'body': "success"
    }
