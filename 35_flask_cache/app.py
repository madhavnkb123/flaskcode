from flask import Flask,jsonify
from functools import lru_cache
import time
app=Flask(__name__)
@lru_cache(maxsize=32)
def expensive(n): time.sleep(1); return n*n
@app.get("/square/<int:n>")
def square(n):
    start=time.perf_counter(); value=expensive(n)
    return jsonify(value=value,seconds=round(time.perf_counter()-start,4),cache=expensive.cache_info()._asdict())
if __name__=="__main__": app.run()