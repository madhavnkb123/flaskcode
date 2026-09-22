from flask import Flask,request,jsonify
app=Flask(__name__)
@app.get("/calculate")
def calc():
    a=float(request.args["a"]); b=float(request.args["b"]); op=request.args["op"]
    if op=="+": r=a+b
    elif op=="-": r=a-b
    elif op=="*": r=a*b
    elif op=="/":
        if b==0:return jsonify(error="division by zero"),400
        r=a/b
    else:return jsonify(error="unsupported operator"),400
    return jsonify(result=r)
if __name__=="__main__": app.run(debug=True)