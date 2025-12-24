# FastAPI CRUD Backend

## 📌 Project Overview
This project is a **simple CRUD (Create, Read, Update, Delete) backend API** built using **FastAPI**.
It is created as a **learning and practice project** to understand how to build REST APIs, connect to a database, and handle backend logic using Python.

This repository is **not a production application**.  
It is intended for **learning, experimentation, and demonstration purposes**.

---

## 🎯 Purpose of the Project
- Learn FastAPI fundamentals
- Practice REST API development
- Understand database integration using SQLAlchemy
- Explore request validation using Pydantic
- Get hands-on experience with backend architecture

---

## 🛠 Tech Stack
- **Language:** Python
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **API Documentation:** Swagger UI
- **Server:** Uvicorn

---

## 🏗 Architecture Overview
- FastAPI handles HTTP requests and responses
- SQLAlchemy manages database operations
- PostgreSQL is used as the local database
- Pydantic validates request and response schemas
- Swagger UI provides interactive API documentation

---

## 📂 Project Structure
Fast-API/
│
├── main.py # FastAPI application entry point
├── models.py # Pydantic models
├── database.py # Database connection
├── database_models.py # SQLAlchemy models
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ Installation Steps

1️ Clone the repository
    bash
   git clone https://github.com/<preethimn9741-debug>/Fast-API.git
   cd Fast-API
   
2️ Create a virtual environment
       python -m venv venv
       
3️ Activate the virtual environment
       venv\Scripts\activate
       
4️ Install dependencies
       pip install -r requirements.txt
       
5 Run the Application
    The API will start at:
        http://127.0.0.1:8000
        uvicorn main:app --reload
        
🧪 How to Test the API
FastAPI provides built-in interactive documentation.
Open your browser
Go to:
http://127.0.0.1:8000/docs
Use Swagger UI to test API endpoints

📌 Example API Endpoints
GET /products → Fetch all products
POST /products → Create a new product
PUT /products/{id} → Update a product
DELETE /products/{id} → Delete a product

🧹 Dependencies Note
This project is purely backend-focused.
Node.js is NOT required
If package.json they can be safely removed

🧪 Testing (Future Enhancement)
Automated tests can be added using:
pytest
httpx or fastapi.testclient

🎨 Code Quality (Optional)
For better formatting and linting:
black – code formatter
flake8 – linter

📌 Conclusion
This project is a learning-focused FastAPI backend that demonstrates how to build and run a CRUD API using Python and PostgreSQL.
It is ideal for:
Beginners learning FastAPI
Backend practice
Interview demonstrations


       
