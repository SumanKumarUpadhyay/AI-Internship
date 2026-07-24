# Salary Prediction System

## Project Overview

This project is a simple Machine Learning application built using Python and Scikit-learn. It predicts an employee's salary based on their years of experience using the Linear Regression algorithm.

---

## Learning Objectives

- Understand Supervised Machine Learning
- Learn Train-Test Split
- Build a Linear Regression Model
- Make Predictions
- Evaluate Model Performance
- Save the Trained Model

---

## Dataset

The dataset contains two columns:

- YearsExperience (Input Feature)
- Salary (Target Variable)

Example:

| YearsExperience | Salary |
|-----------------|--------|
| 1 | 25000 |
| 2 | 30000 |
| 3 | 35000 |
| 4 | 42000 |
| 5 | 48000 |

---

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## Machine Learning Workflow

1. Load Dataset
2. Check Missing Values
3. Select Features and Target
4. Split Dataset into Training and Testing Data
5. Train Linear Regression Model
6. Make Predictions
7. Evaluate Model
8. Save Model using Joblib

---

## Performance Metrics

The model was evaluated using:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Example:

- MSE : 3056789.45
- RMSE : 1748.36
- R² Score : 0.97

---

## Files

- ml_basics.ipynb
- salary_prediction.py
- salary_dataset.csv
- model.pkl
- README.md

---

## How to Run

### Install Required Library

```bash
pip install scikit-learn
```

### Train the Model

Run:

```
ml_basics.ipynb
```

This will create:

```
model.pkl
```

### Predict Salary

Run:

```
salary_prediction.py
```

Enter:

```
Years of Experience
```

The program will predict the salary.

---

## Sample Output

```
Enter Years of Experience: 5

Predicted Salary: 48500
```

---

## Conclusion

This project demonstrates the basic Machine Learning workflow using Scikit-learn. It helps understand data loading, model training, prediction, evaluation, and model saving using a simple Linear Regression algorithm.