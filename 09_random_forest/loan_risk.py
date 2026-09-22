import pandas as pd
from sklearn.ensemble import RandomForestClassifier
df=pd.DataFrame({"income":[25,30,40,50,60,80,100,120,35,75],"debt":[20,25,30,35,20,15,10,5,40,18],"approved":[0,0,0,1,1,1,1,1,0,1]})
m=RandomForestClassifier(n_estimators=100,random_state=42).fit(df[["income","debt"]],df.approved)
print("Approval:",m.predict([[45,28]])[0],"Probability:",m.predict_proba([[45,28]])[0].round(2))
