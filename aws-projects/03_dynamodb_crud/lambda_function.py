import boto3,os
table=boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
def lambda_handler(event,context):
    op=event.get("operation","scan")
    if op=="create": table.put_item(Item=event["item"]); return {"statusCode":201,"item":event["item"]}
    if op=="get": return {"statusCode":200,"item":table.get_item(Key={"id":event["id"]}).get("Item")}
    if op=="delete": table.delete_item(Key={"id":event["id"]}); return {"statusCode":204}
    return {"statusCode":200,"items":table.scan().get("Items",[])}
