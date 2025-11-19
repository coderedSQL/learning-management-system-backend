Learning Management System (LMS) – Backend API

A full-featured Django REST Framework backend that implements modern API practices such as a custom user model, JWT authentication, permissions, filtering, search, ordering, pagination, and auto-generated API documentation.

This project was built step-by-step following a complete backend roadmap.

---

🚀 Features

**1. Custom User Model (Most Important Part)**

The project replaces Django’s default user with a **CustomUser model** that supports:

* `username`
* `email`
* `password` (hashed)
* `age`
* `bio`
* `role` (student/instructor/admin)

🔐 Secure Password Handling

Passwords are never stored as plain text.
A custom serializer handles hashing:

```python
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'age', 'bio', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # 🔒 important hashing step
        user.save()
        return user
```

This ensures the user’s password is safely hashed before saving.

---

🔑 JWT Authentication (SimpleJWT)

The project uses **SimpleJWT** for login, token refresh, and secure access.

Endpoints include:

* `/api/auth/register/`
* `/api/auth/login/`
* `/api/auth/token/refresh/`
* Protected routes requiring `Bearer <token>`

---

👮 Permissions & Access Control

The project uses:

* `IsAuthenticated`
* Role-based access (admin, instructor, student)
* Object-level permissions (ownership checks)

Examples:

* Students can only view their own data
* Instructors can manage their own courses
* Admins have full access

---

🔎 Filtering, Search & Ordering

DjangoFilter + DRF Search + Ordering are applied globally.

Example (User list):

* Filter by `role`, `age`
* Search by `username`, `email`
* Order by `username`, `email`

Query examples:

```
/api/users/?search=banu
/api/users/?role=student
/api/users/?ordering=email
```

---

📄 Pagination

Custom pagination using DRF PageNumberPagination:

* Default page size: 10
* Client can control page size
* Max page size: 100

Example:

```
/api/users/?page=2&page_size=5
```

---

📚 API Documentation (Swagger / Redoc)

Interactive documentation included using **drf-yasg**:

* `/swagger/`
* `/redoc/`

---

📘 Project Structure

```
lms_api/
│   manage.py
│   db.sqlite3
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── filters.py
│   └── urls.py
│
├── courses/
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
└── lms_api/
    ├── settings.py
    ├── urls.py
    └── asgi.py
```

---

⚙️ Installation & Setup

1. Clone the project

```
git clone https://github.com/<your-username>/learning-management-system-backend.git
cd learning-management-system-backend
```
2. Install dependencies

```
pip install -r requirements.txt
```

3. Apply migrations

```
python manage.py migrate
```

4. Start the server

```
python manage.py runserver
```

---

🧪 Testing

Use:

* Django admin
* DRF browsable API
* Postman
* Swagger UI

---


🎯 This project includes:

✔ Django models
✔ Migrations
✔ Admin customization
✔ DRF API setup
✔ Serializers
✔ ViewSets
✔ Custom user model
✔ JWT authentication
✔ Permissions & Object-level auth
✔ Filtering, Search, Ordering
✔ Pagination
✔ API documentation
✔ Complete full backend project (LMS)

---

📬 Author

Developed by **banumariwan**
For backend learning, DRF mastery, and real-world API experience.
