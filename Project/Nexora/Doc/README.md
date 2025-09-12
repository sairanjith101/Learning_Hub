
# Nexora

**Nexora** is a Django + Django REST Framework based e‑commerce backend (minimal, production-ready patterns) that provides user authentication (JWT), product/catalog management, wishlist, cart & checkout, orders, payments and coupon management. This README contains setup, usage, API reference, environment variables, deployment notes, and development tips.

> Project location in this archive: `myapi_project/` — project package `nexora/`.  
> **Important:** the repository in the zip includes a `venv/` folder and other environment artefacts. Remove `venv/` before pushing to remote.

---

## Table of contents

1. [Quick summary & features](#quick-summary--features)  
2. [Tech stack](#tech-stack)  
3. [Requirements](#requirements)  
4. [Project structure](#project-structure)  
5. [Initial setup (local development)](#initial-setup-local-development)  
6. [Environment variables (.env sample)](#environment-variables-env-sample)  
7. [Database setup (MySQL) & migrations](#database-setup-mysql--migrations)  
8. [Run server](#run-server)  
9. [API documentation (Swagger / ReDoc)](#api-documentation-swagger--redoc)  
10. [Available endpoints (summary)](#available-endpoints-summary)  
11. [Authentication (JWT) — example requests](#authentication-jwt----example-requests)  
12. [Tests](#tests)  
13. [Development notes & tips](#development-notes--tips)  
14. [Troubleshooting](#troubleshooting)  
15. [Contributing & License](#contributing--license)

---

## Quick summary & features

- Django 5.2 based project (`nexora` project)
- Apps included:
  - `accounts` — registration, JWT login (Simple JWT), profile (`/api/auth/`)
  - `products` — categories, brands, products, wishlist (`/api/catalog/`)
  - `cart` — cart & checkout (`/api/`)
  - `orders` — orders, payments, coupons (`/api/`)
- API documentation available (Swagger & ReDoc).
- JWT authentication using `djangorestframework_simplejwt`.
- MySQL support (PyMySQL driver included in `requirements.txt`).
- Rate limiting configured on registration view.

---

## Tech stack

- Python 3.11+ (project used 3.11 in venv)
- Django 5.2.5
- Django REST Framework
- djangorestframework-simplejwt (for JWT)
- MySQL (PyMySQL)
- tzdata, sqlparse, and other common libraries

See `requirements.txt` at the project root.

---

## Requirements

Install system requirements:

- Python 3.11+ (install via pyenv or system package)
- MySQL server (or use Docker container)
- `pip` and `virtualenv` are recommended

---

## Project structure (important files & folders)

```
myapi_project/
├─ manage.py
├─ requirements.txt
├─ nexora/                 # Django project package (settings, urls)
├─ accounts/               # user registration, login, profile
├─ products/               # products, categories, brands, wishlist
├─ cart/                   # cart, checkout
├─ orders/                 # orders, payments, coupons
├─ venv/                   # ⚠️ remove before committing/pushing
└─ errors.log              # build/dev log (optional to inspect)
```

Key files:
- `nexora/settings.py` — main settings (JWT, REST_FRAMEWORK config, logging)
- `nexora/urls.py` — url routing including Swagger/Redoc
- `accounts/urls.py` — `register/`, `login/` (JWT), `refresh/`, `me/`
- `products/urls.py` — router for `categories`, `brands`, `products`, `wishlist`
- `cart/urls.py` — router for `cart`, `checkout`
- `orders/urls.py` — router for `orders`, `payments`, `coupons`

---

## Initial setup (local development)

1. Extract repo (already done); `cd` into project root (where `manage.py` is):

```bash
cd path/to/myapi_project
```

2. Create & activate virtual environment (recommended):

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install Python dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Create `.env` file (see sample below) and ensure the settings load environment variables (the settings in this project already expect DB credentials and SECRET_KEY — update accordingly).

---

## Environment variables (.env sample)

Create a `.env` (or export env vars) with the following variables (example):

```
# Django secret & debug
DJANGO_SECRET_KEY=replace_this_with_a_secure_random_value
DJANGO_DEBUG=True

# Database (MySQL)
DB_ENGINE=mysql
DB_NAME=nexora_db
DB_USER=nexora_user
DB_PASSWORD=strongpassword
DB_HOST=127.0.0.1
DB_PORT=3306

# Allowed hosts (comma separated)
ALLOWED_HOSTS=localhost,127.0.0.1

# Other optional (email, external services)
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=you@example.com
EMAIL_HOST_PASSWORD=yourpassword
```

> Note: the project uses `PyMySQL` driver. If you prefer `mysqlclient` change requirements & settings accordingly.

---

## Database setup (MySQL) & migrations

1. Create database and user (example MySQL commands):

```sql
CREATE DATABASE nexora_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'nexora_user'@'localhost' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON nexora_db.* TO 'nexora_user'@'localhost';
FLUSH PRIVILEGES;
```

2. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create a superuser:

```bash
python manage.py createsuperuser
```

---

## Run server

```bash
# Development server
python manage.py runserver 0.0.0.0:8000
```

Open:
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

---

## API documentation (Swagger / ReDoc)

The project includes Swagger and ReDoc endpoints registered in `nexora/urls.py`:

- Swagger UI: `/swagger/`
- ReDoc UI: `/redoc/`

Use these UIs to explore the API, view serializers, responses, and test endpoints.

---

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

## Authentication (JWT) — example requests

1. Register (example):

```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"strongpass"}'
```

2. Obtain token:

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"strongpass"}'
```

Response:
```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

3. Use token to call protected endpoint:

```bash
curl -H "Authorization: Bearer <access_token>" http://127.0.0.1:8000/api/auth/me/
```

4. Refresh token:

```bash
curl -X POST http://127.0.0.1:8000/api/auth/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"<refresh_token>"}'
```

---

## Running tests

If tests are included, run:

```bash
python manage.py test
```

(There is a `test.py` at project root — review it. If the project contains pytest or custom test runners adjust accordingly.)

---

## Development notes & tips

- Remove the `venv/` directory before committing. Commit only source code and a clean `requirements.txt`.
- There is an `errors.log` file — check it if migrations or startup had problems.
- Settings: `nexora/settings.py` contains REST_FRAMEWORK config and `SIMPLE_JWT` lifetimes — change as needed.
- Rate limiting: registration uses `django_ratelimit` decorator to reduce abuse — adjust policy in `accounts/views.py`.
- Use the Swagger UI to test serializers and required fields rather than guessing payloads.

---

## Troubleshooting

- `ModuleNotFoundError` or incompatible packages: recreate virtualenv & run `pip install -r requirements.txt`.
- Database connection errors: ensure MySQL is running, credentials are correct, and host/port match `.env`.
- If static files, email or payment providers are used in production, update settings for production (DEBUG=False, allowed hosts, secure cookies, CSRF, HTTPS).

---

## Security / Production Checklist

- Set `DJANGO_DEBUG=False`.
- Set a strong `DJANGO_SECRET_KEY` in environment variables.
- Use HTTPS and set `SECURE_SSL_REDIRECT=True`, `SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`.
- Remove or rotate any secrets committed accidentally.
- Do not commit `venv/`, `.env`, or other secrets.

---

## Notes & suggestions

- The project zip included `venv/` — remove before pushing. Add `venv/` and other env files to `.gitignore`.
- Consider adding a `docker-compose.yml` to simplify local dev (service for MySQL + Django).
- Add CI (GitHub Actions) for linting, tests and migrations check.
- Add an explicit `README.md` to the repository root (this file is intended to be that README).
- If you want, I can also:
  - generate a `.env.example` file,
  - create a `docker-compose.yml` for local testing,
  - prepare a `.gitignore` tuned for Django (exclude `venv/`, `__pycache__`, `.env`, `*.pyc`, etc.),
  - or produce an API reference snippet with sample requests for each endpoint automatically extracted from the code.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

