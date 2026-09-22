import boto3,os
sqs=boto3.client("sqs")
def lambda_handler(event,context):
    r=sqs.send_message(QueueUrl=os.environ["QUEUE_URL"],MessageBody=str(event.get("message","Hello SQS")))
    return {"statusCode":200,"message_id":r["MessageId"]}
