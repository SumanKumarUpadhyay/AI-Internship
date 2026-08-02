# API Testing Report

## Project
Loan Prediction API using Flask & FastAPI

## Objective

The objective of this testing was to verify that the Prediction API correctly processes valid inputs, handles invalid inputs gracefully, and returns appropriate responses.

---

# Testing Environment

- Framework: Flask & FastAPI
- Testing Tool: Swagger UI / Thunder Client
- API Method: POST
- Endpoint: /predict

---

# Test Cases

| Test Case | Input | Expected Result | Status |
|-----------|-------|-----------------|--------|
| 1 | Valid loan details | Loan Prediction | Passed |
| 2 | Different income value | Loan Prediction | Passed |
| 3 | High CIBIL Score | Loan Approved | Passed |
| 4 | Low CIBIL Score | Loan Rejected | Passed |
| 5 | Different loan amount | Prediction Generated | Passed |
| 6 | Missing assets field | Validation Error | Passed |
| 7 | Missing income field | Validation Error | Passed |
| 8 | String instead of integer | Validation Error | Passed |
| 9 | Empty JSON | Validation Error | Passed |
| 10 | Negative values | Error Response | Passed |

---

# Sample Valid Request

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

# Sample Response

```json
{
    "prediction": "Loan Approved"
}
```

---

# Invalid Request Example

```json
{
    "education": 1
}
```

---

# Response

```json
{
    "detail": "Validation Error"
}
```

---

# API Testing Summary

- Successfully tested valid requests.
- Successfully handled invalid requests.
- Verified JSON request and response.
- Confirmed prediction generation.
- Confirmed validation and error handling.

## Conclusion

The Loan Prediction API was successfully tested using multiple valid and invalid inputs. The API correctly predicted loan status for valid requests and returned meaningful validation errors for incorrect inputs.