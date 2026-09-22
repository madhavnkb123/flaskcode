import boto3,os
sns=boto3.client("sns")
def lambda_handler(event,context):
    sns.publish(TopicArn=os.environ["TOPIC_ARN"],Subject="AWS Alert",Message=event.get("message","Test notification"))
    return {"statusCode":200,"message":"SNS notification sent"}
