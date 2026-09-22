import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
df=pd.DataFrame({"customer":["C1","C2","C3","C4","C5","C6"],"spend":[1200,300,2500,450,1800,700],"orders":[12,3,20,5,15,7]})
X=StandardScaler().fit_transform(df[["spend","orders"]])
df["segment"]=KMeans(n_clusters=3,n_init=10,random_state=42).fit_predict(X)
print(df.sort_values("segment"))
