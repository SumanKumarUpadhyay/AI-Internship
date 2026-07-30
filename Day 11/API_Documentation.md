# Employee REST API Documentation

## Base URL

http://127.0.0.1:5000

---

## GET

### Endpoint

GET /employees

### Description

Returns all employee records.

### Response

Status Code : 200 OK

Example

[
    {
        "id":1,
        "name":"Suman",
        "role":"AI Engineer"
    }
]

---

## POST

### Endpoint

POST /employees

### Description

Adds a new employee.

### Request

{
    "id":2,
    "name":"Rahul",
    "role":"Data Analyst"
}

### Response

Status Code : 201 Created

{
    "message":"Employee Added Successfully"
}

---

## PUT

### Endpoint

PUT /employees/<id>

### Description

Updates employee details.

Status Code

200 OK

404 Not Found

---

## DELETE

### Endpoint

DELETE /employees/<id>

### Description

Deletes employee data.

Status Code

200 OK

404 Not Found