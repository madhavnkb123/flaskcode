from flask import Flask,request,jsonify
app=Flask(__name__)
positive={"good","great","excellent","happy","love","awesome","success"}
negative={"bad","poor","terrible","sad","hate","awful","fail"}
@app.post("/sentiment")
def sentiment():
    text=request.get_json().get("text","").lower(); words=set(text.split())
    score=len(words&positive)-len(words&negative)
    return jsonify(score=score,sentiment="positive" if score>0 else "negative" if score<0 else "neutral")
if __name__=="__main__": app.run(debug=True)