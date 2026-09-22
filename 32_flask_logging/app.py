import logging
from flask import Flask,jsonify
app=Flask(__name__)
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
log=app.logger
@app.get("/api/status")
def status():
    log.info("status endpoint called"); return jsonify(status="running")
if __name__=="__main__": app.run()