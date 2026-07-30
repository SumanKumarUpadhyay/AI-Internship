from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    role: str

employees = [
    {
        "id": 1,
        "name": "Suman Kumar",
        "role": "AI/ML Intern"
    },
    {
        "id": 2,
        "name": "Rahul Sharma",
        "role": "Data Analyst"
    }
]

@app.get("/")
def home():
    return {"message": "Welcome to Employee REST API"}

@app.get("/employees")
def get_employees():
    return employees

@app.post("/employees")
def add_employee(employee: Employee):

    employees.append(employee.dict())

    return {
        "message": "Employee Added Successfully",
        "employee": employee
    }

@app.put("/employees/{id}")
def update_employee(id: int, updated_employee: Employee):

    for employee in employees:

        if employee["id"] == id:

            employee["name"] = updated_employee.name
            employee["role"] = updated_employee.role

            return {
                "message": "Employee Updated Successfully",
                "employee": employee
            }

    return {
        "message": "Employee Not Found"
    }