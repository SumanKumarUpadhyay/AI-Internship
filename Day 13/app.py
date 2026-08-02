from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("C:\\Users\\suman\\Desktop\\Ai - Internship\\AI-Internship\\Day 13\\dt_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return "Loan Prediction API is Running!"


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        df = pd.DataFrame([data])

        prediction = model.predict(df)[0]

        if prediction == 1:
            result = "Loan Approved"
        else:
            result = "Loan Rejected"

        return jsonify({
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)