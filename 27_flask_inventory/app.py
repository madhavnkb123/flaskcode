from flask import Flask,request,jsonify
app=Flask(__name__); items={}
@app.post("/items")
def add():
    d=request.get_json(); i=str(d["id"]); items[i]=d; return jsonify(d),201
@app.get("/items")
def all_items(): return jsonify(list(items.values()))
@app.patch("/items/<i>")
def update(i):
    if i not in items:return jsonify(error="not found"),404
    items[i].update(request.get_json()); return jsonify(items[i])
@app.delete("/items/<i>")
def delete(i):
    if i not in items:return jsonify(error="not found"),404
    return jsonify(items.pop(i))
if __name__=="__main__": app.run(debug=True)