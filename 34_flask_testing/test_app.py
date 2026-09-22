import unittest
from flask import Flask,jsonify
app=Flask(__name__)
@app.get("/health")
def health(): return jsonify(status="ok")
class TestApp(unittest.TestCase):
    def setUp(self): app.testing=True; self.client=app.test_client()
    def test_health(self):
        r=self.client.get("/health"); self.assertEqual(r.status_code,200); self.assertEqual(r.json["status"],"ok")
if __name__=="__main__": unittest.main()