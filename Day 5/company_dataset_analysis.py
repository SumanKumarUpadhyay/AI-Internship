import pandas as pd

# Load Dataset
df = pd.read_csv("C:\\Users\\suman\\Desktop\\Ai - Internship\\AI-Internship\\Day 5\\company_dataset.csv")

print(" First 5 Rows")
print(df.head())

print("\n----- Dataset Information -----")
df.info()

print("\n----- Statistical Summary -----")
print(df.describe())

print("\n----- Missing Values -----")
print(df.isnull().sum())