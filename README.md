# 🎓 Django Students API

> **Project Name:** Django Students API  
> **Author:** Robiul Hossain  
> **Course:** BISEW Scholarship Programme  
> **ID:** 1287940  
> **Round:** 65

---

## 🚀 Project Overview

Django Students API is a robust, scalable **REST API** built with **Django 6** and **Django REST Framework (DRF)** to manage student data.

**Key Features:**
- ✅ CRUD operations for students
- 🌐 Browsable API with DRF
- 🗂 JSON response format
- 🔐 Admin panel integration
- ⚡ Easily extendable

---

## 🛠 Tech Stack

| Layer       | Technology |
|------------|------------|
| Backend     | Python 3.12, Django 6.x |
| API         | Django REST Framework |
| Database    | SQLite / PostgreSQL / MySQL |
| Dependencies| djangorestframework |
| Tools       | VS Code, Postman, Git |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/django-students-api.git
cd django-students-api

2️⃣ Create virtual environment
python -m venv venv

3️⃣ Activate virtual environment

Windows:

venv\Scripts\activate


Linux / Mac:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create superuser (admin)
python manage.py createsuperuser

7️⃣ Run server
python manage.py runserver

🗂 Project Structure
myproject/
├── students/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt

🌐 API Endpoints

Base URL: http://127.0.0.1:8000/api/students/

Method	Endpoint	Description	Request Body Example
GET	/api/students/	List all students	None
POST	/api/students/	Create new student	{ "name": "John Doe", "age": 22, "email": "john@example.com" }
GET	/api/students/<id>/	Retrieve student	None
PUT	/api/students/<id>/	Update student details	{ "name": "Jane Doe", "age": 23 }
PATCH	/api/students/<id>/	Partial update student	{ "age": 24 }
DELETE	/api/students/<id>/	Delete a student	None
📄 Example JSON Responses

1️⃣ GET /api/students/

[
  {
    "id": 1,
    "name": "John Doe",
    "age": 22,
    "email": "john@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "age": 23,
    "email": "jane@example.com"
  }
]


2️⃣ POST /api/students/

{
  "id": 3,
  "name": "Alice Brown",
  "age": 21,
  "email": "alice@example.com"
}

🔒 Authentication & Permissions

By default, DRF allows browsable API access.

Production-ready authentication: JWT / Token

Example:

from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

📝 Admin Panel

Access: http://127.0.0.1:8000/admin/

Manage students easily without API calls

Requires superuser

🧩 Best Practices

Use virtual environments

Keep secrets in .env files

Modular apps for scalability (students, accounts)

Always write tests

Add pagination & filtering for large datasets

📌 Requirements
Django>=6.0
djangorestframework>=3.15

⭐ Future Enhancements

JWT Authentication

Filtering & search

Pagination

Swagger / Redoc API documentation