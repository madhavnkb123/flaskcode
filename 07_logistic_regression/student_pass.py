import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report
df=pd.DataFrame({"attendance":[55,60,65,70,75,80,85,90,92,95],"hours":[1,2,2,3,4,4,5,6,7,8],"passed":[0,0,0,1,1,1,1,1,1,1]})
Xtr,Xte,ytr,yte=train_test_split(df[["attendance","hours"]],df["passed"],test_size=.3,random_state=42)
m=LogisticRegression().fit(Xtr,ytr); p=m.predict(Xte)
print("Accuracy:",accuracy_score(yte,p)); print(classification_report(yte,p,zero_division=0))
