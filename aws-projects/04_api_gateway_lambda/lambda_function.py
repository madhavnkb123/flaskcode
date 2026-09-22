import json
def lambda_handler(event,context):
    method=event.get("requestContext",{}).get("http",{}).get("method","GET")
    return {"statusCode":200,"headers":{"Content-Type":"application/json"},"body":json.dumps({"message":"AWS API is working","method":method})}
