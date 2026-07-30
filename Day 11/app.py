from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route("/")
def home():
    return "Welcome to Employee REST API"

@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

@app.route("/employees", methods=["POST"])
def add_employee():

    new_employee = request.get_json()

    employees.append(new_employee)

    return jsonify({
        "message": "Employee Added Successfully",
        "employee": new_employee
    }), 201

@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    updated_data = request.get_json()

    for employee in employees:

        if employee["id"] == id:

            employee["name"] = updated_data["name"]
            employee["role"] = updated_data["role"]

            return jsonify({
                "message": "Employee Updated Successfully",
                "employee": employee
            })

    return jsonify({
        "message": "Employee Not Found"
    }), 404
if __name__ == "__main__":
    app.run(debug=True)