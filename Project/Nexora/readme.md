# Nexora – Multi-Vendor E-Commerce Backend (Django + DRF)

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-5.2-green)
![DRF](https://img.shields.io/badge/DRF-3.x-red)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Nexora** is a Django + Django REST Framework based e-commerce backend providing:

* **User authentication (JWT)**
* **Product/catalog management**
* **Wishlist, cart & checkout**
* **Orders, payments, coupons**

This README contains setup, usage, API reference, environment variables, deployment notes, and development tips.

> 📂 Project root: `myapi_project/`
> ⚠️ Remove `venv/` and other environment artifacts before pushing to GitHub.

---

## Table of Contents

1. [Quick summary & features](#quick-summary-features)
2. [Tech stack](#tech-stack)
3. [Project structure](#project-structure)
4. [Initial setup](#initial-setup)
5. [Environment variables](#environment-variables)
6. [Database setup & migrations](#database-setup-migrations)
7. [Run server](#run-server)
8. [API documentation](#api-documentation)
9. [Authentication examples](#authentication-examples)
10. [Development notes](#development-notes)
11. [Troubleshooting](#troubleshooting)
12. [Security checklist](#security-checklist)
13. [License](#license-)

---

## Quick Summary & Features

* Django 5.2 project (`nexora`)
* Role-based APIs:

  * **Accounts** → registration, JWT login/refresh, profile
  * **Products** → categories, brands, products, wishlist
  * **Cart** → cart operations & checkout
  * **Orders** → orders, payments, coupons
* Swagger & ReDoc documentation
* JWT authentication (`djangorestframework-simplejwt`)
* MySQL support (via PyMySQL)
* Rate limiting on registration endpoint

---

## 🛠 Tech Stack

* **Backend:** Python 3.11, Django 5.2, Django REST Framework
* **Auth:** JWT (SimpleJWT)
* **Database:** MySQL (PyMySQL; optionally SQLite/PostgreSQL)
* **Docs:** Swagger & ReDoc
* **Testing:** Django test framework / pytest

---

## 📂 Project Structure

```
myapi_project/
├─ manage.py
├─ requirements.txt
├─ LICENSE
├─ nexora/                 # Django project (settings, urls)
├─ accounts/               # authentication & profiles
├─ products/               # categories, brands, products, wishlist
├─ cart/                   # cart & checkout
├─ orders/                 # orders, payments, coupons
├─ venv/                   # ⚠️ remove before committing
└─ errors.log              # optional dev log
```

Key files:

* `nexora/settings.py` → main config (JWT, REST, logging)
* `nexora/urls.py` → routes (Swagger/Redoc included)
* App `urls.py` → API routes per module

---

## ⚙️ Initial Setup

```bash
cd myapi_project
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\Activate.ps1  # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

`.env` sample:

```env
DJANGO_SECRET_KEY=replace_me
DJANGO_DEBUG=True
DB_ENGINE=mysql
DB_NAME=nexora_db
DB_USER=nexora_user
DB_PASSWORD=strongpassword
DB_HOST=127.0.0.1
DB_PORT=3306
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 🗄 Database Setup & Migrations

```sql
CREATE DATABASE nexora CHARACTER SET utf8mb4;
CREATE USER 'nexora_user'@'%' IDENTIFIED BY 'StrongPassword123!';
GRANT ALL PRIVILEGES ON nexora.* TO 'nexora_user'@'%';
FLUSH PRIVILEGES;
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## ▶️ Run Server

```bash
python manage.py runserver
```

* Swagger → [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
* ReDoc → [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 📖 API Documentation

Full API details, serializers, and query params are visible in Swagger & ReDoc.

## Available endpoints (summary)

### Accounts (Authentication)
Base: `/api/auth/`
- `POST /api/auth/register/` — user registration
- `POST /api/auth/login/` — obtain JWT access & refresh tokens (SimpleJWT)
- `POST /api/auth/refresh/` — refresh JWT token
- `GET|PUT /api/auth/me/` — get/update logged-in user profile (auth required)

### Products / Catalog
Base: `/api/catalog/`
- `GET /api/catalog/categories/` — list/create categories (viewset)
- `GET /api/catalog/brands/` — list/create brands
- `GET /api/catalog/products/` — list/create products; supports retrieve, update (viewset)
- `GET|POST /api/catalog/wishlist/` — wishlist endpoints (viewset)

> These are wired using DRF router; check the Swagger UI for route details and query params.

### Cart & Checkout
Base: `/api/`
- `GET|POST /api/cart/` — cart operations (viewset)
- `GET|POST /api/checkout/` — checkout endpoints (viewset)

### Orders, Payments, Coupons
Base: `/api/`
- `GET|POST /api/orders/` — orders viewset
- `GET|POST /api/payments/` — payments viewset
- `GET|POST /api/coupons/` — coupons viewset

---

## 🔐 Authentication Examples

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"strongpass"}'

# Login
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"strongpass"}'
```

---

## 💡 Development Notes

* Add `.gitignore` (exclude `venv/`, `.env`, `__pycache__/`, `*.pyc`, logs).
* `errors.log` is for local debugging.
* Adjust JWT lifetimes in `settings.py`.
* Rate limiting enabled for registration endpoint.

---

## 🚑 Troubleshooting

* Reinstall dependencies: `pip install -r requirements.txt`
* Ensure DB is running & credentials are correct
* For production: `DEBUG=False`, set `ALLOWED_HOSTS`, enable HTTPS

---

## 🔒 Security Checklist

* Use a strong `DJANGO_SECRET_KEY`
* Enable HTTPS (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`)
* Never commit `.env` or `venv/`

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for full details.

