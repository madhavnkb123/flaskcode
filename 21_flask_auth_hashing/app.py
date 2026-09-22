from flask import Flask,request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
app=Flask(__name__)
users={}
@app.post("/register")
def register():
    d=request.get_json() or {}; u=d.get("username"); p=d.get("password")
    if not u or not p:return jsonify(error="username/password required"),400
    if u in users:return jsonify(error="user exists"),409
    users[u]=generate_password_hash(p); return jsonify(message="registered"),201
@app.post("/login")
def login():
    d=request.get_json() or {}; h=users.get(d.get("username"))
    return jsonify(authenticated=bool(h and check_password_hash(h,d.get("password",""))))
if __name__=="__main__": app.run(debug=True)