from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)
MODEL_PATH = os.path.join("models", "fault_detector.pkl")
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    probability = None

    if request.method == "POST":
        try:
            values = [
                float(request.form["voltage"]),
                float(request.form["current"]),
                float(request.form["resistance"]),
                float(request.form["temperature"]),
                float(request.form["frequency"]),
                float(request.form["vibration"])
            ]
            prediction = model.predict([values])[0]
            probabilities = model.predict_proba([values])[0]
            probability = round(max(probabilities) * 100, 2)
            result = "FAULTY COMPONENT" if prediction == 1 else "NORMAL COMPONENT"
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)
