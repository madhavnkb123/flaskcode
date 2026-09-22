from flask import Flask,render_template
app=Flask(__name__)
@app.get("/")
def dashboard():
    data={"sales":125000,"orders":840,"customers":320,"conversion":6.4}
    return render_template("dashboard.html",**data)
if __name__=="__main__": app.run(debug=True)