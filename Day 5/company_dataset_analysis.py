import pandas as pd

# Load Dataset
df = pd.read_csv("C:\\Users\\suman\\Desktop\\Ai - Internship\\AI-Internship\\Day 5\\company_dataset.csv")

print(" First 5 Rows")
print(df.head())

print("Dataset Information")
df.info()

print("Statistical Summary ")
print(df.describe())

print(" Missing Values")
print(df.isnull().sum())