import pandas as pd
df=pd.DataFrame({"product":["A","B","A","C","B","A"],"region":["West","East","West","North","East","South"],"sales":[1200,900,1500,700,1100,1800]})
df["sales"]=pd.to_numeric(df["sales"])
print("Summary:\n",df.groupby("product")["sales"].agg(["sum","mean","count"]))
print("\nRegion totals:\n",df.groupby("region")["sales"].sum().sort_values(ascending=False))
print("\nTop sale:\n",df.loc[df["sales"].idxmax()])
