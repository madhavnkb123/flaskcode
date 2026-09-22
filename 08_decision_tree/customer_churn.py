import pandas as pd
from sklearn.tree import DecisionTreeClassifier
df=pd.DataFrame({"tenure":[2,4,8,12,18,24,30,36],"support":[5,4,3,2,2,1,1,0],"churn":[1,1,1,0,0,0,0,0]})
m=DecisionTreeClassifier(max_depth=3,random_state=42).fit(df[["tenure","support"]],df.churn)
print("Prediction for tenure=6, support=4:",m.predict([[6,4]])[0])
print("Feature importance:",dict(zip(["tenure","support"],m.feature_importances_.round(2))))
