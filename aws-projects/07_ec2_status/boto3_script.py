import boto3
ec2=boto3.client("ec2")
for r in ec2.describe_instances()["Reservations"]:
    for i in r["Instances"]:
        print(i["InstanceId"],i["State"]["Name"],i.get("InstanceType"))
