# 🛒 Nexora – Multi-Vendor E-Commerce Backend (Django + DRF)

## 📌 Project Overview

**Nexora** is a **multi-vendor e-commerce backend** built with **Django** and **Django REST Framework (DRF)**.
It supports multiple user roles (**Admin, Seller, Customer**) and provides APIs for:

* User & vendor management
* Product handling (by sellers)
* Cart management (by customers)
* Order placement (checkout flow ready for extension)

The backend is API-first, making it easy to integrate with frontend apps (React, Angular, Next.js) or mobile apps (Flutter, React Native).

---

## 🚀 Features

* **User & Vendor Accounts**

  * Admin can create/manage users
  * Sellers can register and add products
  * Customers can browse and purchase products
* **Cart Management**

  * Add/update/remove products in cart
  * Cart linked to user session
* **Authentication**

  * Login & registration APIs
  * Role-based access (Admin, Seller, Customer)
* **API-First**

  * Built with DRF for clean and structured REST APIs
* **Error Logging**

  * Centralized logging with `errors.log`

---

## 📂 Project Structure

```
nexora_project/
│── manage.py
│── requirements.txt
│── errors.log
│
│── nexora/                # Main project configuration
│   ├── settings.py
│   ├── urls.py
│
│── accounts/              # User & Vendor management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
│── cart/                  # Cart management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-nexora-repo-url>
cd nexora_project
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Create superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server

```bash
python manage.py runserver
```

Server will be running at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🔑 API Endpoints

### Authentication (Accounts App)

* `POST /accounts/register/` → Register (Admin/Seller/Customer)
* `POST /accounts/login/` → Login (returns token/session)
* `GET /accounts/users/` → View all users (Admin only)

### Seller (Vendor)

* `POST /products/` → Add new product
* `PUT /products/{id}/` → Update product
* `GET /products/my/` → View own products

### Customer

* `GET /products/` → Browse products
* `POST /cart/` → Add item to cart
* `PUT /cart/{id}/` → Update quantity
* `GET /cart/` → View cart
* `POST /orders/` → Checkout

---

## 🧑‍💻 Postman Testing (Role-Based)

* **Admin**

  * Create Seller & Customer accounts
* **Seller**

  * Login → Add products → Manage stock
* **Customer**

  * Login → Browse products → Add to cart → Checkout

👉 Use **Authorization: Bearer <token>** in headers for protected routes.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** SQLite (can be switched to MySQL/PostgreSQL)
* **API Testing:** Postman
* **Authentication:** Django Auth (JWT ready)

---

## 📌 Future Enhancements

* Product Reviews & Ratings
* Payment Gateway Integration (Stripe/Razorpay)
* Celery for background tasks (order emails, notifications)
* Redis caching for scalability

---

## 📜 License

This project is for **educational/demo purposes**.

---