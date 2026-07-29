# Import Libraries
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("C:\\Users\\suman\\Desktop\\Ai - Internship\\AI-Internship\\Day 9\\movie_reviews.csv")

# Features and Target
X = df["review"]
y = df["sentiment"]

# Convert Text into Numbers
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = MultinomialNB()

model.fit(X_train, y_train)

# Model Accuracy
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# User Input
review = input("\nEnter Movie Review: ")

# Convert Input
review_vector = vectorizer.transform([review])

# Predict
prediction = model.predict(review_vector)

print("\nPrediction:", prediction[0])