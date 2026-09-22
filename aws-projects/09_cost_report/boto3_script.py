import boto3
from datetime import datetime,timedelta
ce=boto3.client("ce")
end=datetime.utcnow().date(); start=end-timedelta(days=7)
r=ce.get_cost_and_usage(TimePeriod={"Start":str(start),"End":str(end)},Granularity="DAILY",Metrics=["UnblendedCost"])
for day in r["ResultsByTime"]:
    print(day["TimePeriod"]["Start"],day["Total"]["UnblendedCost"]["Amount"],day["Total"]["UnblendedCost"]["Unit"])
