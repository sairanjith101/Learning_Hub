# MugilVault – Cloud Storage System Backend (Django + DRF)

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-5.2-green)
![DRF](https://img.shields.io/badge/DRF-3.x-red)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**MugilVault** is a secure, scalable cloud storage system built with Django and DRF. It provides user authentication and file management features with RESTful APIs.  

This README covers setup, usage, API reference, environment variables, deployment notes, and dev tips.  

> 📂 Project root: `MugilVault/`  
> ⚠️ Remove `venv/` and other environment artifacts before pushing to GitHub.  

---

## Table of Contents

1. [Quick summary & features](#quick-summary--features)  
2. [Tech stack](#tech-stack)  
3. [Project structure](#project-structure)  
4. [Initial setup](#initial-setup)  
5. [Environment variables](#environment-variables)  
6. [Database setup & migrations](#database-setup--migrations)  
7. [Run server](#run-server)  
8. [API documentation](#api-documentation)  
9. [Authentication examples](#authentication-examples)  
10. [Development notes](#development-notes)  
11. [Troubleshooting](#troubleshooting)  
12. [Security checklist](#security-checklist)  
13. [License](#license)  

---

## Quick summary & features

- User Registration and Authentication (JWT)
- Upload, Download, Delete, Rename and List Files
- Advanced Storage Features (see API docs)
- Swagger & Redoc API documentation
- Local media storage support (for development)
- Easy API testing with Postman collection

---

## Tech stack

* **Backend:** Python 3.11, Django 5.x, Django REST Framework  
* **Auth:** JWT (SimpleJWT)  
* **Database:** MySQL → can be swapped with SQLite/PostgreSQL  
* **Docs:** Swagger / Postman collection   

---

## Project structure

```
MugilVault/
├─ manage.py
├─ requirements.txt
├─ LICENSE
├─ README.md
├─ .env
├─ mugilvault/            # Django project (settings, urls, wsgi, asgi)
├─ users/                 # user authentication & profiles
├─ storage/               # storage & permission-based access
├─ media/uploads/         # uploaded files
└─ .gitignore
```

Key files:

* `mugilvault/settings.py` → main config (REST, JWT, DB)  
* `mugilvault/urls.py` → API routes, Swagger docs  
* `storage/views.py` → file operations APIs  
* `users/models.py` → custom user model  

---

## Initial setup

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\Activate.ps1  # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Environment variables

Sample `.env`:

```env
DJANGO_SECRET_KEY=replace_me
DJANGO_DEBUG=True
DB_ENGINE=sqlite3
DB_NAME=db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## Database setup & migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## Run server

```bash
python manage.py runserver
```

* Swagger → [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  
* Admin panel → [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

---

## API documentation

Available endpoints (summary):  

### Users (Authentication)  
Base: `/api/users/`  
- `POST /api/auth/register/` → create account  
- `POST /api/auth/login/` → obtain JWT tokens  
- `POST /api/auth/refresh/` → refresh token   

### Storage  
Base: `/api/files/`  
- `POST /api/files/` → upload  
- `GET /api/files/` → list  
- `GET /api/files/<id>/` → retrieve
- `PUT /api/files/<id>/` → replace file
- `PATCH /api/files/<id>/` → update file name/metadata  
- `DELETE /api/files/<id>/` → delete
- `GET /api/files/usage/` → usage details
- `GET /api/files/<id>/share/` → expirey link   

---

## Authentication examples

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/auth/register/   -H "Content-Type: application/json"   -d '{"username":"username","email":"user@example.com","password":"strongpass"}'

# Login
curl -X POST http://127.0.0.1:8000/api/auth/login/   -H "Content-Type: application/json"   -d '{"email":"user@example.com","password":"strongpass"}'
```

---

## Development notes

* Add `.gitignore` (exclude `venv/`, `.env`, `__pycache__/`, `*.pyc`, `logs/`)  
* Uploaded files stored in `/media/uploads/` (configure `MEDIA_ROOT` in `.env`)  
* JWT settings can be tuned in `settings.py`  

---

## Troubleshooting

* If dependencies mismatch: `pip install -r requirements.txt`  
* If DB errors: check `.env` config & run migrations  
* For production: set `DEBUG=False`, configure `ALLOWED_HOSTS`, use HTTPS  

---

## Security checklist

* Use a strong `DJANGO_SECRET_KEY`  
* Enable HTTPS (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`)  
* Never commit `.env` or `venv/`  

---

## License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.  
