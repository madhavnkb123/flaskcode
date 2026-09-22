import boto3,os
cw=boto3.client("cloudwatch")
def lambda_handler(event,context):
    cw.put_metric_data(Namespace="MyApplication",MetricData=[{"MetricName":"Requests","Value":1,"Unit":"Count"}])
    return {"statusCode":200,"message":"Metric published"}
