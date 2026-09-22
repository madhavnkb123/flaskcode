from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42, stratify=data.target
)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=500))
model.fit(X_train, y_train)

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok", accuracy=round(float(model.score(X_test, y_test)), 3))

@app.post("/predict")
def predict():
    payload = request.get_json() or {}
    features = payload.get("features")
    if not isinstance(features, list) or len(features) != 4:
        return jsonify(error="features must contain 4 numeric values"), 400
    prediction = int(model.predict([features])[0])
    return jsonify(prediction=prediction, label=data.target_names[prediction])

if __name__ == "__main__":
    app.run(debug=True)