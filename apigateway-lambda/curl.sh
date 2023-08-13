#!/bin/bash

# API_KEY is the API key generated in the API Gateway console
API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxx"
API_ENDPOINT="https://xxxxxxxxxxxxxxxxxxxxx.com/Prod/get"
curl -X GET "$API_ENDPOINT" -H "x-api-key: $API_KEY"
