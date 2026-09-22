from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

DATA_FILE = "data/students.csv"
GRAPH_FILE = "static/student_performance.png"

def load_data():
    return pd.read_csv(DATA_FILE)

def analyze_data():
    df = load_data()

    df["average"] = np.mean(df[["python", "data_science", "flask"]], axis=1)

    def get_grade(mark):
        if mark >= 90:
            return "A+"
        elif mark >= 80:
            return "A"
        elif mark >= 70:
            return "B"
        elif mark >= 60:
            return "C"
        return "D"

    df["grade"] = df["average"].apply(get_grade)

    python_avg = df["python"].mean()
    data_science_avg = df["data_science"].mean()
    flask_avg = df["flask"].mean()

    top_student = df.loc[df["average"].idxmax()]

    os.makedirs("static", exist_ok=True)

    subjects = ["Python", "Data Science", "Flask"]
    averages = [python_avg, data_science_avg, flask_avg]

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, averages)
    plt.title("Average Student Performance")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(GRAPH_FILE)
    plt.close()

    return df, round(python_avg, 2), round(data_science_avg, 2), round(flask_avg, 2), top_student

@app.route("/")
def home():
    df = load_data()
    return render_template("index.html", students=df.to_dict(orient="records"))

@app.route("/analysis")
def analysis():
    df, python_avg, data_science_avg, flask_avg, top_student = analyze_data()
    return render_template(
        "analysis.html",
        students=df.to_dict(orient="records"),
        python_avg=python_avg,
        data_science_avg=data_science_avg,
        flask_avg=flask_avg,
        top_student=top_student.to_dict()
    )

@app.route("/api/students")
def students_api():
    df = load_data()
    df["average"] = np.mean(df[["python", "data_science", "flask"]], axis=1)
    return df.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)
