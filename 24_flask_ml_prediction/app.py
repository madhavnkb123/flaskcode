from flask import Flask,request,jsonify
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
app=Flask(__name__)
x,y=load_iris(return_X_y=True); model=RandomForestClassifier(n_estimators=100,random_state=42).fit(x,y)
@app.post("/predict")
def predict():
    v=request.get_json()["features"]; p=int(model.predict([v])[0])
    return jsonify(class_id=p,class_name=load_iris().target_names[p])
if __name__=="__main__": app.run(debug=True)