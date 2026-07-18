
# Employee Salary Management
employees = {
    "Suman": 50000,
    "Aman": 45000,
    "Riya": 60000,
    "Priya": 55000
}
# to display employee details 
def display_employees():
    print("\nEmployee Details")

    for name, salary in employees.items():
        print(f"{name} : ₹{salary}")


# Function to calculate average salary
def average_salary():
    salaries = list(employees.values())     
    average = sum(salaries) / len(salaries)

    print(f"\nAverage Salary : ₹{average:.2f}")


# Function to find highest salary
def highest_salary():
    highest_employee = max(employees, key=employees.get)

    print("\nHighest Salary")
    print(f"Employee : {highest_employee}")
    print(f"Salary   : ₹{employees[highest_employee]}")


# Main Function
def main():


    print(" EMPLOYEE SALARY MANAGEMENT SYSTEM ")
    

    display_employees()
    average_salary()
    highest_salary()


# Run Program
main()