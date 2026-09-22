from flask import Flask,Response
import csv,io
app=Flask(__name__)
@app.get("/export")
def export():
    out=io.StringIO(); w=csv.writer(out); w.writerow(["id","name","score"])
    for r in [(1,"Asha",88),(2,"Ravi",92),(3,"Neha",79)]: w.writerow(r)
    return Response(out.getvalue(),mimetype="text/csv",headers={"Content-Disposition":"attachment; filename=students.csv"})
if __name__=="__main__": app.run()