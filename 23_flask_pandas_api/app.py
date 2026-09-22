from flask import Flask,jsonify,request
import pandas as pd
app=Flask(__name__)
df=pd.DataFrame({"name":["Asha","Ravi","Neha"],"score":[82,91,74]})
@app.get("/students")
def students():
    q=request.args.get("q","").lower()
    x=df[df.name.str.lower().str.contains(q)] if q else df
    return jsonify(x.to_dict("records"))
@app.get("/stats")
def stats(): return jsonify(mean=float(df.score.mean()),max=int(df.score.max()),min=int(df.score.min()))
if __name__=="__main__": app.run(debug=True)