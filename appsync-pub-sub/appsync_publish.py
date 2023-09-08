from graphqlclient import GraphQLClient

# AppSyncエンドポイントのURL
api_url = 'https://qs5j6ypbeffdlancp3z6uo2xue.appsync-api.ap-northeast-1.amazonaws.com/graphql'
api_key = "da2-ke5wea5kzbffpbosy72nipzfmu"

def execute_query_api(gql_client):
    query = """
        query MyQuery {
        getItem(id: "") {
            id
            message
            }
        }
    """
    result = gql_client.execute(query)
    print(result)
    
def execute_mutation_api(gql_client):
    
    #AWSの画面からコピーしてくる
    mutation = """
        mutation MyMutation {
            addItem(text: "") {
            id
            text
            }
        }
    """
    variables = {
        "text": "hello world",
    }
        
    print("set data=",variables)
    result = gql_client.execute(mutation,variables=variables)
    print("result=",result)
    
if __name__ == '__main__':
    c = GraphQLClient(api_url)
    c.inject_token(api_key, 'X-Api-Key')

    # 登録する 
    execute_mutation_api(c)

    # 登録した情報を取得する
    execute_query_api(c)
