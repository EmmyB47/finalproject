from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__, template_folder="../templates")

DATA_PATH = os.getenv("DATA_PATH", "assets/broadway.csv")

df = pd.read_csv(DATA_PATH)

# Build dropdown options (example: show titles)
OPTIONS = sorted(df["Show.Name"].dropna().unique())

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    if request.method == "POST":
        selected = request.form.get("choice")
        result = df[df["Show.Name"] == selected].to_dict(orient="records")

    return render_template("index.html", options=OPTIONS, result=result)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
