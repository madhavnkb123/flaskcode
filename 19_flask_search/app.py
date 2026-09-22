from flask import Flask,request,render_template_string
app=Flask(__name__)
products=["Python Course","Flask Course","Data Science Course","AWS Course","Machine Learning Course"]
HTML="""<form><input name=q value='{{q}}'><button>Search</button></form><ul>{% for p in results %}<li>{{p}}</li>{% endfor %}</ul>"""
@app.get("/")
def search():
 q=request.args.get("q","").lower(); return render_template_string(HTML,q=q,results=[p for p in products if q in p.lower()])
app.run(debug=True)
