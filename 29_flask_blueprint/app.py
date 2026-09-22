from flask import Flask,Blueprint,jsonify
api=Blueprint("api",__name__,url_prefix="/api")
@api.get("/health")
def health(): return jsonify(status="ok")
@api.get("/courses")
def courses(): return jsonify(courses=["Python","Flask","Data Science"])
app=Flask(__name__); app.register_blueprint(api)
if __name__=="__main__": app.run(debug=True)