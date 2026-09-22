import pandas as pd
df=pd.DataFrame({"salary":[25000,30000,32000,35000,36000,38000,40000,45000,200000]})
q1,q3=df.salary.quantile([.25,.75]); iqr=q3-q1
lo,hi=q1-1.5*iqr,q3+1.5*iqr
print("Bounds:",lo,hi); print("Outliers:\n",df[(df.salary<lo)|(df.salary>hi)])
