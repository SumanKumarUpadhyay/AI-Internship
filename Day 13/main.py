from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle

# Create FastAPI app
app = FastAPI(
    title="Loan Prediction API",
    description="Predict Loan Approval using a Decision Tree Model",
    version="1.0"
)

# Load trained model
with open("dt_model.pkl", "rb") as file:
    model = pickle.load(file)


# Input Schema
class LoanInput(BaseModel):
    no_of_dependents: int
    education: int
    income_annum: float
    loan_amount: float
    loan_term: int
    cibil_score: int
    assets: float


@app.get("/")
def home():
    return {"message": "Loan Prediction API is Running!"}


@app.post("/predict")
def predict(data: LoanInput):

    try:
        # Convert input to DataFrame
        df = pd.DataFrame([data.model_dump()])

        # Predict
        prediction = model.predict(df)[0]

        result = "Loan Approved" if prediction == 1 else "Loan Rejected"

        return {
            "prediction": result
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))