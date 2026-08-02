# Day 13 - Model Serialization & Prediction API

## Overview

On Day 13, I learned how to deploy a trained Machine Learning model as a REST API using Flask and FastAPI. I used the Decision Tree model trained on Day 8, serialized it using Pickle, and created prediction APIs for loan approval.

---

## Learning Objectives

- Model Serialization
- Pickle
- Prediction APIs
- Flask
- FastAPI
- Error Handling
- API Testing

---

## Project

### Loan Prediction API

A Machine Learning API that predicts whether a loan will be **Approved** or **Rejected** based on applicant details.

The model was trained using a **Decision Tree Classifier** and saved as a Pickle (`.pkl`) file.

---

## Input Features

- Number of Dependents
- Education
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Assets

---

## Output

Example Response

```json
{
    "prediction": "Loan Approved"
}
```

---

## Technologies Used

- Python
- Flask
- FastAPI
- Pickle
- Pandas
- Scikit-learn
- Uvicorn
- Swagger UI

---

## Project Structure

```
Day 13/
│
├── app.py                  # Flask Prediction API
├── main.py                 # FastAPI Prediction API
├── dt_model.pkl            # Serialized Decision Tree Model
├── loan_check.csv          # Sample Dataset
├── README.md
├── API_Testing_Report.md
├── Edge_Cases.md
├── requirements.txt
└── screenshots/
```

---

## API Endpoints

### Flask

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home Page |
| POST | /predict | Predict Loan Status |

---

### FastAPI

| Method | Endpoint |
|---------|----------|
| GET | / |
| POST | /predict |
| Swagger UI | /docs |

---

## Example Request

```json
{
    "no_of_dependents": 2,
    "education": 1,
    "income_annum": 9600000,
    "loan_amount": 29900000,
    "loan_term": 12,
    "cibil_score": 778,
    "assets": 50700000
}
```

---

## Example Response

```json
{
    "prediction": "Loan Approved"
}
```

---

## Features

- Load trained ML model using Pickle
- Prediction using Flask API
- Prediction using FastAPI
- JSON request and response
- Error handling
- Swagger API documentation
- REST API testing

---

## Files

- `app.py` - Flask API
- `main.py` - FastAPI API
- `dt_model.pkl` - Trained Decision Tree model
- `loan_check.csv` - Sample dataset
- `API_Testing_Report.md`
- `Edge_Cases.md`

---

## Conclusion

Successfully deployed a Decision Tree Machine Learning model using both Flask and FastAPI. Implemented prediction APIs, handled JSON requests and responses, added error handling, and tested the APIs using different valid and invalid inputs. This project demonstrates the complete workflow of deploying a serialized ML model as a REST API.