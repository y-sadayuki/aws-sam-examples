import appsync_wss_wrapper
import time,uuid
import base64
import json

API_URL = "https://qs5j6ypbeffdlancp3z6uo2xue.appsync-api.ap-northeast-1.amazonaws.com/graphql"
WSS_URL = API_URL.replace("https","wss").replace("appsync-api","appsync-realtime-api")
API_KEY = 'da2-ke5wea5kzbffpbosy72nipzfmu'

if __name__ == "__main__":

    print("sub")

    #ホスト名だけを取得
    appsync_host = API_URL.replace('https://', '').replace('wss://', '')
    appsync_host = appsync_host.replace('/graphql', '')

    appsync_client = appsync_wss_wrapper.AppSyncWssClient(appsync_host, WSS_URL,API_KEY)

    ##ランダムなハッシュ値を作成
    #sub_id = str(uuid.uuid4())
    #query = make_subscription_query(sub_id)

    ##websocket作成
    #ws = websocket.WebSocketApp( connection_url,subprotocols=["graphql-ws"])
    #ws.on_open = create_on_open(query)
    #ws.on_close = on_close
    #ws.on_message = on_message

    #ws.run_forever()
## 以下のURLの実装を参考にしています。
## https://aws.amazon.com/jp/blogs/mobile/appsync-websockets-python/

#API_URL="https://qs5j6ypbeffdlancp3z6uo2xue.appsync-api.ap-northeast-1.amazonaws.com/graphql"
#WSS_URL = API_URL.replace("https","wss").replace("appsync-api","appsync-realtime-api")

## AppSyncのエンドポイントURL
#appsync_endpoint = WSS_URL  

#appsync_host = API_URL.replace('https://', '').replace('wss://', '')
#appsync_host = appsync_host.replace('/graphql', '')

#print("appsync_host:", appsync_host)
#print("")

##指定した文字列を除去するコード
#def remove_str(text, remove_str):
    #return text.replace(remove_str, '')


## AppSyncのAPIキー
#api_key = 'da2-ke5wea5kzbffpbosy72nipzfmu'

##ヘッダー情報作成
#header_dict = dict()
#header_dict['host'] = appsync_host
#header_dict["x-api-key"] = api_key

##dict型を文字列に変換
#header_str = json.dumps(header_dict)

##Base64エンコード
#header_bytes = base64.b64encode(header_str.encode("utf-8"))
#header_str = header_bytes.decode("utf-8")
#connection_url = WSS_URL + '?header=' + header_str + '&payload=e30='

#print("connection_url:", connection_url)
#print("")

## サブスクリプションクエリ
#subscription_query = dict()
#subscription_query['query'] = '''
    #subscription MySubscription {
        #onGetItem {
        #text
        #id
        #}
    #}
#'''

#subscription_query['query'] = '''
    #MyQuery {
        #getItem(id: "") {
        #id
        #text
        #}
    #}
#'''

## GraphQL subscription Registration object
#GQL_SUBSCRIPTION = json.dumps({
        #'query': 'subscription MySubscription {onGetItem{id text}}',
        #'variables': {}
#})


## GraphQL subscription Registration object
#GQL_QUERY = json.dumps({
        #'query': 'query MyQuery { getItem{id text} }',
        #'variables': {}
#})

#subscription_query['variables'] = dict()

#def make_subscription_query(id):

    #register = {
        #'id': id,
        #'payload': {
            #'data': GQL_SUBSCRIPTION,
            #'extensions': {
                #'authorization': {
                    #'host': appsync_host,
                    #'x-api-key': api_key,
                #}
            #}
        #},
        #'type': 'start'
    #}

    ##dict型を文字列に変換
    #return json.dumps(register)

##register = '''
##{
    ##'id': SUB_ID,
    ##'payload': {
        ##'data': GQL_SUBSCRIPTION,
        ##'extensions': {
            ##'authorization': {
                ##'host':HOST,
                ##'x-api-key':API_KEY
            ##}
        ##}
    ##},
    ##'type': 'start'
##}
##'''


#def create_on_open(message):
    #def on_open(ws):
        #print("WebSocket connection opened")
        #print("message:", message)
        #hogehoge = message 
        #ws.send(hogehoge)
    #return on_open

#def on_message(ws,message):
    #print("on message:", message)

#def on_error(ws, message):
    #print("on error message:", message)

#def on_close(ws, message):
    #print("on close message:", message)

#if __name__ == "__main__":

    ##ランダムなハッシュ値を作成
    #sub_id = str(uuid.uuid4())
    #query = make_subscription_query(sub_id)

    ##websocket作成
    #ws = websocket.WebSocketApp( connection_url,subprotocols=["graphql-ws"])
    #ws.on_open = create_on_open(query)
    #ws.on_close = on_close
    #ws.on_message = on_message

    #ws.run_forever()