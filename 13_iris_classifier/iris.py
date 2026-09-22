from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
d=load_iris()
Xtr,Xte,ytr,yte=train_test_split(d.data,d.target,test_size=.25,random_state=42,stratify=d.target)
m=RandomForestClassifier(n_estimators=100,random_state=42).fit(Xtr,ytr)
print("Accuracy:",accuracy_score(yte,m.predict(Xte)))
print("Sample:",d.target_names[m.predict([[5.1,3.5,1.4,0.2]])[0]])
