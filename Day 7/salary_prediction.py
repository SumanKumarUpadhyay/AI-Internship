import joblib

# Load the trained model
model = joblib.load("C:\\Users\\suman\\Desktop\\Ai - Internship\\AI-Internship\\Day 7\\model.pkl")

# Take input
experience = float(input("Enter Years of Experience: "))

# Predict salary
salary = model.predict([[experience]])

# Print result
print("Predicted Salary:", salary[0])