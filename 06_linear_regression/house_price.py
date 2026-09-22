import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
df=pd.DataFrame({"area":[800,1000,1200,1500,1800,2200,2500,3000],"price":[35,42,50,62,75,90,105,130]})
X=df[["area"]]; y=df["price"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42)
m=LinearRegression().fit(Xtr,ytr); p=m.predict(Xte)
print("MAE:",mean_absolute_error(yte,p),"R2:",r2_score(yte,p))
print("2500 sqft:",m.predict([[2500]])[0])
