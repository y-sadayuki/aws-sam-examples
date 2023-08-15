# api-gateway+lambdaをIP認証ありで構築する場合のテンプレート



template.yamlの以下の部分でIP許可するIPを追加する。複数ある場合はカンマ区切り
<pre>
 Environment:
        Variables:
          ALLOWED_IPS: "192.168.1.1,xxx.xxx.xxx.xxx"
</pre>

ipはipcheck.shを実行すれば確認できる。

<pre>
# ./ipcheck.sh
 xxx.xxx.xxx.xxx
</pre>

"deploy --guided"の初回の設定を行う。 認証に関する質問は"y"で答える必要あり。
<pre>
# deploy --guided (初回のみ)
</pre>
<pre>
InputFunction has no authentication. Is this okay?[y/N]
</pre>

2回目以降は"--guided"は省略可になる。
<pre>
# deploy (2回目以降)
</pre>

curlでデプロイされたエンドポイントにアクセスすれば"Hello World"がかえってくる
<pre>
# curl https://xxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/Prod/inputa

hello world
</pre>


・AWS Serverless Application Modelのドキュメント<br>
https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/what-is-concepts.html

・
'ReadMe自動生成
https://murasan-net.com/index.php/2023/03/24/gpt-4-github-readme-md/

・appsync確認
aws appsync get-graphql-api --api-id 2bshnius4nhwhli2ivwqxeaata