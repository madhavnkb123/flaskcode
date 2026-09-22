from flask import Flask,jsonify,request
app=Flask(__name__); users=[{"id":1,"name":"Akhil"},{"id":2,"name":"Natasha"}]
@app.get("/api/users")
def all_users(): return jsonify(users)
@app.get("/api/users/<int:user_id>")
def get_user(user_id):
 u=next((x for x in users if x["id"]==user_id),None)
 return jsonify(u) if u else ({"error":"User not found"},404)
@app.post("/api/users")
def add_user():
 data=request.get_json(); new={"id":max([u["id"] for u in users],default=0)+1,"name":data["name"]}; users.append(new); return jsonify(new),201
app.run(debug=True)
