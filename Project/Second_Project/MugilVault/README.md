# MugilVault – Secure Storage & User Management Backend (Django + DRF)

![Python](https://img.shields.io/badge/python-3.11-blue)  
![Django](https://img.shields.io/badge/django-5.x-green)  
![DRF](https://img.shields.io/badge/DRF-3.x-red)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)  

**MugilVault** is a Django + Django REST Framework backend designed for **secure storage operations** and **user account management**.  
It provides APIs for authentication, file storage, and permission-based access control.  

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

* Django 5.x project (`mugilvault`)  
* Core modules:  
  - **Users** → registration, JWT login, profile management  
  - **Storage** → file uploads, secure access, permission system  
* REST APIs with DRF + JWT (SimpleJWT)  
* Swagger API docs included  
* Media file storage under `/media/uploads/`  

---

## Tech stack

* **Backend:** Python 3.11, Django 5.x, Django REST Framework  
* **Auth:** JWT (SimpleJWT)  
* **Database:** SQLite (default) → can be swapped with MySQL/PostgreSQL  
* **Docs:** Swagger / Postman collection  
* **Testing:** Django test framework  

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
├─ Doc/                   # extra docs (swagger, features, postman, etc.)
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
cd MugilVault
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
MEDIA_ROOT=media/
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
- `POST /api/users/register/` → create account  
- `POST /api/users/login/` → obtain JWT tokens  
- `POST /api/users/refresh/` → refresh token  
- `GET|PUT /api/users/me/` → profile operations  

### Storage  
Base: `/api/storage/`  
- `POST /api/storage/upload/` → upload files  
- `GET /api/storage/list/` → list uploaded files  
- `GET /api/storage/<id>/` → retrieve single file info  
- `DELETE /api/storage/<id>/` → delete file  

---

## Authentication examples

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/users/register/   -H "Content-Type: application/json"   -d '{"email":"user@example.com","password":"strongpass"}'

# Login
curl -X POST http://127.0.0.1:8000/api/users/login/   -H "Content-Type: application/json"   -d '{"email":"user@example.com","password":"strongpass"}'
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
