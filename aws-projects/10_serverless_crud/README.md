# AWS Serverless CRUD

Architecture:

API Gateway -> Lambda -> DynamoDB

This follows the AWS serverless CRUD pattern. API Gateway routes HTTP requests to Lambda, and Lambda reads/writes DynamoDB. Configure IAM permissions for Lambda before deployment.

Suggested routes:
GET /items
GET /items/{id}
PUT /items
DELETE /items/{id}

Official AWS tutorial:
https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html
