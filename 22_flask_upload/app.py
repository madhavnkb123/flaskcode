from flask import Flask,request,jsonify
from pathlib import Path
from werkzeug.utils import secure_filename
app=Flask(__name__); UP=Path("uploads"); UP.mkdir(exist_ok=True)
ALLOWED={"csv","txt","pdf","png","jpg","jpeg"}
@app.post("/upload")
def upload():
    f=request.files.get("file")
    if not f:return jsonify(error="file required"),400
    ext=f.filename.rsplit(".",1)[-1].lower() if "." in f.filename else ""
    if ext not in ALLOWED:return jsonify(error="file type not allowed"),415
    name=secure_filename(f.filename); f.save(UP/name)
    return jsonify(filename=name),201
if __name__=="__main__": app.run(debug=True)