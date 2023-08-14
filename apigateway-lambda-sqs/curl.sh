#!/bin/bash

# API_KEY is the API key generated in the API Gateway console
API_KEY="t42X1MJ2Zv3coOSzaNK9q3Vw9isjogHf6kX3Uhefa"
API_ENDPOINT="https://dga3ciz6n6.execute-api.ap-northeast-1.amazonaws.com/Prod/push"

DATA='{"key1": "value1", "key2": "value2"}'

#curl -X GET  "$API_ENDPOINT" -H "x-api-key: $API_KEY"
curl -X POST  "$API_ENDPOINT" -d "$DATA" -H "x-api-key: $API_KEY" -H "Content-Type: application/json"
