import os
from flask import Flask,jsonify
app=Flask(__name__)
@app.get("/environment")
def environment():
    return jsonify(app_env=os.getenv("APP_ENV","development"),debug=os.getenv("DEBUG","false").lower()=="true")
if __name__=="__main__": app.run(debug=os.getenv("DEBUG","false").lower()=="true")