# 🛒 Nexora – Multi-Vendor E-Commerce Backend (Django + DRF)

## 📌 Overview
**Nexora** is a **multi-vendor e-commerce backend** built with **Django** and **Django REST Framework (DRF)**.  
It provides role-based APIs for **Admins, Sellers, and Customers**, making it suitable for e-commerce apps (React, Next.js, Flutter, etc.).

---

## 🚀 Features
- **User & Vendor Accounts**
  - Admin → manage users/vendors  
  - Seller → add/manage products  
  - Customer → browse & purchase  
- **Cart Management** → add, update, remove items  
- **Orders** → checkout flow (extensible)  
- **Authentication** → JWT-based login & register  
- **Error Logging** → centralized log file (`errors.log`)  

---

## 🧑‍🤝‍🧑 Roles
- **Admin** → Manage all users and vendors  
- **Seller** → Create and manage own products  
- **Customer** → Browse products, manage cart, place orders  

---

## 📂 Project Structure
```
nexora_project/
│── manage.py
│── requirements.txt
│── errors.log
│
│── nexora/        # Project settings & URLs
│── accounts/      # User & role management
│── cart/          # Cart & order logic
```

---

## ⚙️ Setup Instructions
### 1️⃣ Clone repo
```bash
git clone <your-repo-url>
cd nexora_project
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
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

### 6️⃣ Run server
```bash
python manage.py runserver
```
Server → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 API Endpoints
### Authentication
- `POST /accounts/register/` → Register user  
- `POST /accounts/login/` → Login (returns JWT)  
- `GET /accounts/users/` → List users (Admin only)  

### Seller
- `POST /products/` → Add product  
- `PUT /products/{id}/` → Update product  
- `GET /products/my/` → List own products  

### Customer
- `GET /products/` → Browse all products  
- `POST /cart/` → Add item to cart  
- `PUT /cart/{id}/` → Update quantity  
- `GET /cart/` → View cart  
- `POST /orders/` → Checkout  

---

## 📌 Minimal Example (cURL)
```bash
# Register
curl -X POST http://127.0.0.1:8000/accounts/register/   -H "Content-Type: application/json"   -d '{"email":"user@example.com","password":"mypassword"}'

# Login
curl -X POST http://127.0.0.1:8000/accounts/login/   -H "Content-Type: application/json"   -d '{"email":"user@example.com","password":"mypassword"}'
```

Use returned token:
```
Authorization: Bearer <your_token>
```

---

## 🛠️ Tech Stack
- **Backend:** Python, Django, DRF  
- **Database:** SQLite (switchable to MySQL/PostgreSQL)  
- **Auth:** JWT Authentication  
- **API Testing:** Postman  

---

## 📌 Future Enhancements
- Product reviews & ratings  
- Payment gateway integration  
- Background jobs (emails, notifications)  

---

## 📜 License
This project is for **educational/demo purposes** (MIT License recommended).  
