from flask import Flask,jsonify
app=Flask(__name__)
@app.get("/divide/<float:a>/<float:b>")
def divide(a,b):
    if b==0: raise ValueError("cannot divide by zero")
    return jsonify(result=a/b)
@app.errorhandler(ValueError)
def value_error(e): return jsonify(error=str(e)),400
@app.errorhandler(404)
def not_found(e): return jsonify(error="route not found"),404
if __name__=="__main__": app.run(debug=True)