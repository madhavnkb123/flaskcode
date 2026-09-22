from flask import Flask,request,jsonify
app=Flask(__name__); data=[{"id":i,"name":f"Student {i}"} for i in range(1,101)]
@app.get("/students")
def students():
 page=max(request.args.get("page",1,type=int),1); size=min(request.args.get("size",10,type=int),50)
 start=(page-1)*size; return jsonify({"page":page,"size":size,"total":len(data),"items":data[start:start+size]})
app.run(debug=True)
