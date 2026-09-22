from flask import Flask,jsonify
from flask_cors import CORS
app=Flask(__name__); CORS(app,resources={r"/api/*":{"origins":"*"}})
@app.get("/api/data")
def data(): return jsonify(message="CORS enabled",data=[1,2,3])
if __name__=="__main__": app.run(debug=True)