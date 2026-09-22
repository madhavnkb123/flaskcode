from flask import Flask,request,redirect,url_for,render_template_string
app=Flask(__name__); items=[]; next_id=1
HTML="""<h1>Products</h1><form method=post><input name=name required><input name=price type=number step=.01 required><button>Add</button></form>{% for x in items %}<p>{{x.id}} - {{x.name}} - {{x.price}} <a href='/delete/{{x.id}}'>Delete</a></p>{% endfor %}"""
@app.route("/",methods=["GET","POST"])
def home():
 global next_id
 if request.method=="POST":
  items.append({"id":next_id,"name":request.form["name"],"price":float(request.form["price"])}); next_id+=1; return redirect(url_for("home"))
 return render_template_string(HTML,items=items)
@app.route("/delete/<int:item_id>")
def delete(item_id):
 global items; items=[x for x in items if x["id"]!=item_id]; return redirect(url_for("home"))
app.run(debug=True)
