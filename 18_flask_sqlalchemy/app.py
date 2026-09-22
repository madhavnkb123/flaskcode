from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__); app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///students.db"; db=SQLAlchemy(app)
class Student(db.Model):
 id=db.Column(db.Integer,primary_key=True); name=db.Column(db.String(80),nullable=False); marks=db.Column(db.Float,default=0)
@app.get("/students")
def students(): return jsonify([{"id":s.id,"name":s.name,"marks":s.marks} for s in Student.query.all()])
with app.app_context():
 db.create_all()
 if not Student.query.first(): db.session.add_all([Student(name="Akhil",marks=85),Student(name="Natasha",marks=92)]); db.session.commit()
app.run(debug=True)
