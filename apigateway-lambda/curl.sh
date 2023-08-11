#!/bin/bash

API_KEY="Bvap13tJpc9GrQshKEHO24Y3wiK9CXPu3xdO9jWb"
API_ENDPOINT="https://v1smjjgayh.execute-api.ap-northeast-1.amazonaws.com/Prod/get"

curl -X GET "$API_ENDPOINT" -H "x-api-key: $API_KEY"
#curl -X GET "$API_ENDPOINT" 
