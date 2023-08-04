# AWS SAMテンプレートの練習用

# Tips
- **デプロイ済みのstack明を取得**<br>
aws cloudformation describe-stacks --query "Stacks[].StackName" --output text

- **デプロイ済みスタックの削除**<br>
aws cloudformation delete-stack --stack-name <スタック名>
