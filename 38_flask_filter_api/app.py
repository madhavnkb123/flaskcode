from flask import Flask,request,jsonify
app=Flask(__name__)
products=[{"id":1,"name":"Laptop","category":"electronics","price":65000},{"id":2,"name":"Chair","category":"furniture","price":8000},{"id":3,"name":"Phone","category":"electronics","price":30000}]
@app.get("/products")
def products_api():
    cat=request.args.get("category"); low=float(request.args.get("min_price",0)); high=float(request.args.get("max_price",1e18))
    r=[p for p in products if (not cat or p["category"]==cat) and low<=p["price"]<=high]
    return jsonify(r)
if __name__=="__main__": app.run()