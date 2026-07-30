# Day 11 – REST API Development using Flask & FastAPI

## 📌 Overview

This project demonstrates the development of REST APIs using both **Flask** and **FastAPI**. It covers the basic CRUD (Create, Read, Update, Delete) operations on an Employee Management System.

The project was completed as part of my AI/ML Internship Day 11 task to understand backend web development, REST API concepts, HTTP methods, JSON data exchange, and API testing.

---

## 🎯 Learning Objectives

- Understand REST API architecture
- Learn HTTP methods (GET, POST, PUT, DELETE)
- Build APIs using Flask
- Build APIs using FastAPI
- Understand JSON request and response
- Test APIs using Swagger UI and Thunder Client

---

## 🛠 Technologies Used

- Python 3.x
- Flask
- FastAPI
- Uvicorn
- Pydantic
- Thunder Client / Swagger UI

---

## 📂 Project Structure

```
Day_11/
│
├── app.py                  # Flask REST API
├── main.py                 # FastAPI REST API
├── flask_rest_api.ipynb
├── fastapi_rest_api.ipynb
├── API_Documentation.md
├── README.md
├── requirements.txt
├── thunder_collection.json
└── screenshots/
```

---

## 🚀 Flask API

Run the Flask application:

```bash
python app.py
```

Server:

```
http://127.0.0.1:5000
```

Available Endpoints:

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Welcome Message |
| GET | /employees | Get all employees |
| POST | /employees | Add employee |
| PUT | /employees/{id} | Update employee |

---

## ⚡ FastAPI

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

Available Endpoints:

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Welcome Message |
| GET | /employees | Get all employees |
| POST | /employees | Add employee |
| PUT | /employees/{id} | Update employee |
| DELETE | /employees/{id} | Delete employee |

---

## 📦 Sample Employee JSON

```json
{
  "id": 1,
  "name": "Suman Kumar",
  "role": "AI/ML Intern"
}
```

---

## 📚 Key Concepts Learned

- REST API
- CRUD Operations
- HTTP Methods
- JSON
- Request & Response
- API Testing
- Flask Basics
- FastAPI Basics
- Pydantic Models
- Swagger Documentation

---

## 📈 Learning Outcome

After completing this project, I can:

- Develop REST APIs using Flask and FastAPI.
- Perform CRUD operations.
- Handle JSON request and response.
- Build APIs using Pydantic models.
- Test APIs using Swagger UI and Thunder Client.
- Understand the differences between Flask and FastAPI.

---

## 📌 Conclusion

This project helped me understand how backend APIs are developed and tested using two popular Python frameworks. Flask provided a simple introduction to REST APIs, while FastAPI demonstrated modern API development with automatic validation, interactive documentation, and improved developer productivity.