import os
from flask import Flask,jsonify
class Config:
    SECRET_KEY=os.getenv("SECRET_KEY","dev-secret")
    JSON_SORT_KEYS=False
app=Flask(__name__); app.config.from_object(Config)
@app.get("/config")
def config(): return jsonify(debug=app.debug,environment=os.getenv("FLASK_ENV","development"))
if __name__=="__main__": app.run()