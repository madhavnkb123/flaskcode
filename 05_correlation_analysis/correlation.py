import pandas as pd
df=pd.DataFrame({"hours":[2,3,4,5,6,7,8],"score":[55,60,66,70,78,84,90],"sleep":[8,7,7,6,7,6,6]})
print(df.corr(numeric_only=True).round(2))
