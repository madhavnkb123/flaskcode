from flask import Flask,jsonify,request
from collections import defaultdict
import time
app=Flask(__name__); hits=defaultdict(list); LIMIT=5; WINDOW=60
@app.before_request
def limit():
    ip=request.remote_addr or "unknown"; now=time.time(); hits[ip]=[t for t in hits[ip] if now-t<WINDOW]
    if len(hits[ip])>=LIMIT:return jsonify(error="rate limit exceeded"),429
    hits[ip].append(now)
@app.get("/api/data")
def data(): return jsonify(message="request accepted")
if __name__=="__main__": app.run()