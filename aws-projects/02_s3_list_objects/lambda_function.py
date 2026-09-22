import boto3,os
s3=boto3.client("s3")
def lambda_handler(event,context):
    r=s3.list_objects_v2(Bucket=os.environ["BUCKET_NAME"])
    return {"statusCode":200,"objects":[x["Key"] for x in r.get("Contents",[])]}
