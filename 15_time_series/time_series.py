import pandas as pd
dates=pd.date_range("2026-01-01",periods=8,freq="ME")
df=pd.DataFrame({"date":dates,"sales":[100,120,115,140,155,150,175,190]}).set_index("date")
df["moving_avg"]=df.sales.rolling(3).mean()
print(df)
print("Next-month estimate:",round(df.sales.rolling(3).mean().iloc[-1],2))
