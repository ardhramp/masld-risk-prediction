from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load trained model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model",
    "masld_logistic_model.pkl"
)

model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        feature_order = [
            "Age",
            "Sex",
            "BMI",
            "Waist",
            "Systolic_BP",
            "Diastolic_BP",
            "Glucose",
            "HDL",
            "Total_Cholesterol",
            "Triglycerides",
            "Sedentary_Minutes",
            "Alcohol_Ever"
        ]

        input_data = pd.DataFrame(
            [[data.get(feature) for feature in feature_order]],
            columns=feature_order
        )

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1] * 100

        if prediction == 1:
            result = "High Risk"
        else:
            result = "Low Risk"

        return jsonify({
            "success": True,
            "prediction": result,
            "probability": round(probability, 2)
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)