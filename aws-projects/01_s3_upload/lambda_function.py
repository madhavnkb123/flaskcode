import boto3
import os
s3=boto3.client("s3")
BUCKET=os.environ["BUCKET_NAME"]
def lambda_handler(event,context):
    key=event.get("key","sample.txt")
    body=event.get("body","Hello from Lambda")
    s3.put_object(Bucket=BUCKET,Key=key,Body=body.encode())
    return {"statusCode":200,"body":f"Uploaded {key}"}
