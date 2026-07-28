
# Day 9: Natural Language Processing (NLP) Preprocessing and Sentiment Analysis

## Overview

This project was completed as part of the AI/ML Internship Day 9 tasks.

The objective of this project is to understand the basic concepts of Natural Language Processing (NLP) and build a simple Movie Review Sentiment Classifier using Machine Learning.

---

## Learning Objectives

- Understand Natural Language Processing (NLP)
- Learn Tokenization
- Learn Stopword Removal
- Learn Stemming
- Learn Lemmatization
- Understand TF-IDF
- Build a Sentiment Analysis model

---

## Technologies Used

- Python
- Pandas
- NLTK
- Scikit-learn
- Jupyter Notebook
- VS Code

---

## Project Structure

```
Day_9/
│── nlp_preprocessing.ipynb
│── review_classifier.py
│── movie_reviews.csv
│── screenshots/
│── README.md
```

---

## NLP Preprocessing Techniques

### 1. Tokenization
Splits a sentence into individual words (tokens).

Example:
```
"The movie was amazing."

↓

["The", "movie", "was", "amazing"]
```

---

### 2. Stopword Removal

Removes common words such as:

- the
- is
- was
- and
- in

Example:

```
Original:
The movie was amazing

After Stopword Removal:
movie amazing
```

---

### 3. Stemming

Reduces words to their root form.

Examples:

- playing → play
- amazing → amaz
- enjoyable → enjoy

---

### 4. Lemmatization

Converts words into meaningful dictionary words.

Examples:

- cars → car
- studies → study
- running → running

---

### 5. TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts text into numerical values so that Machine Learning algorithms can understand text data.

---

## Sentiment Analysis

Sentiment Analysis identifies whether a review is:

- Positive
- Negative

Example:

Input:
```
Movie was amazing
```

Output:
```
Positive
```

Input:
```
Worst movie ever
```

Output:
```
Negative
```

---

## Machine Learning Algorithm

- Naive Bayes Classifier

Reason:
- Fast
- Simple
- Works well for text classification problems

---

## Files Description

### nlp_preprocessing.ipynb

Contains:

- Introduction to NLP
- Tokenization
- Stopword Removal
- Stemming
- Lemmatization
- TF-IDF
- Sentiment Analysis
- Conclusion

---

### review_classifier.py

A Python program that:

- Reads movie reviews
- Converts text into TF-IDF vectors
- Trains a Naive Bayes model
- Predicts whether a review is Positive or Negative

---

### movie_reviews.csv

Contains sample movie reviews and their sentiment labels.

---

## Sample Output

```
Model Accuracy: 100%

Enter Movie Review:
Movie was amazing

Prediction:
Positive
```

---

## Applications

- Movie Review Analysis
- Spam Detection
- Email Classification
- Chatbots
- Social Media Analysis
- Product Review Analysis

---

## Learning Outcome

After completing this project, I learned:

- NLP basics
- Text preprocessing techniques
- TF-IDF Vectorization
- Naive Bayes Classification
- Movie Review Sentiment Analysis

---

## Author

**Suman Kumar**

B.Tech CSE (Artificial Intelligence)

Chhattisgarh Swami Vivekanand Technical University (CSVTU)

AI/ML Intern
