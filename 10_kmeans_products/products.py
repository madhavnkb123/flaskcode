import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
df=pd.DataFrame({"product":["P1","P2","P3","P4","P5","P6"],"price":[10,12,100,110,15,105],"rating":[4.1,4.3,4.8,4.7,4.0,4.9]})
X=StandardScaler().fit_transform(df[["price","rating"]])
df["cluster"]=KMeans(n_clusters=2,n_init=10,random_state=42).fit_predict(X)
print(df)
