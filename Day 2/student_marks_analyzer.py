
# Student Marks Analyzer

# Function to calculate highest mark
def highest_mark(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest


# Function to calculate lowest mark
def lowest_mark(marks):
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark
    return lowest


# Function to calculate average mark
def average_mark(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)


# Function to display marks above average
def above_average(marks, average):
    print("\nMarks Above Average:")
    for mark in marks:
        if mark > average:
            print(mark)


# Main Program
marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = int(input(f"Enter marks of Student {i+1}: "))
    marks.append(mark)

highest = highest_mark(marks)
lowest = lowest_mark(marks)
average = average_mark(marks)

print("\n------ Result ------")
print("Highest Marks :", highest)
print("Lowest Marks  :", lowest)
print("Average Marks :", round(average, 2))

above_average(marks, average)