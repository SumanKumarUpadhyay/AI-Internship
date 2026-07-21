import numpy as np

# Input number of students
n = int(input("Enter number of students: "))

# Input marks
marks = []

for i in range(n):
    mark = int(input(f"Enter marks of Student {i+1}: "))
    marks.append(mark)

# Convert list to NumPy array
marks = np.array(marks)

# Display Results
print("\n----- Student Marks Report -----")

print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))