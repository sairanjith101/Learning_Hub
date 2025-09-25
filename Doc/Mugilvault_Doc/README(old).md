# MugilVault - Cloud Storage System

MugilVault is a secure, scalable cloud storage system built with Django and DRF. It provides user authentication and file management features with RESTful APIs. This project is part of the Learning_Hub repository.

## Features

- User Registration and Authentication (JWT)
- Upload, Download, Delete, and List Files
- Advanced Storage Features (see API docs)
- Swagger & Redoc API documentation
- Local media storage support (for development)
- Easy API testing with Postman collection

## Tech Stack

- Python, Django, Django REST Framework
- JWT (Simple JWT)
- Swagger (drf-yasg)
- SQLite (default, can configure other DBs)
- Frontend: Not included (API only)

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/sairanjith101/Learning_Hub.git
cd Learning_Hub/Project/Second_Project/MugilVault
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

### Access API Documentation

- Swagger UI: [`/swagger/`](http://localhost:8000/swagger/)
- Redoc UI: [`/redoc/`](http://localhost:8000/redoc/)

## API Endpoints

### Auth APIs

| Endpoint              | Method | Description           |
|-----------------------|--------|-----------------------|
| `/api/auth/register/` | POST   | User Registration     |
| `/api/auth/login/`    | POST   | Obtain JWT Tokens     |
| `/api/auth/refresh/`  | POST   | Refresh JWT Token     |

#### Example Request (Register)
```json
POST /api/auth/register/
{
  "username": "testuser",
  "password": "yourpassword",
  "email": "user@email.com"
}
```

#### Example Request (Login)
```json
POST /api/auth/login/
{
  "username": "testuser",
  "password": "yourpassword"
}
```

### File Storage APIs

See `/api/` endpoints for file operations. Common ones include:

| Endpoint                    | Method | Description            |
|-----------------------------|--------|------------------------|
| `/api/files/`               | GET    | List files             |
| `/api/files/upload/`        | POST   | Upload file            |
| `/api/files/<id>/`          | GET    | Download file          |
| `/api/files/<id>/`          | DELETE | Delete file            |

> **Note:** Exact endpoints may vary. Refer Swagger UI for full details and parameters.

---

## Postman Collection

- Full Postman API Collection available at:  
  `Project/Second_Project/Doc/3_Postman_API_Collection.rtf`
- Import this file into Postman for ready-to-use API tests.

---

## Advanced Features

- Advanced APIs documented under "MugilVault Advanced Feature APIs" section in the Postman collection file.
- Supports role-based access, metadata queries, and more.

---

## Project Structure

```
Learning_Hub/
└── Project/
    └── Second_Project/
        ├── MugilVault/        # Django project root
        │   ├── mugilvault/    # Project settings, URLs
        │   ├── users/         # User management
        │   ├── storage/       # Storage app (files)
        │   └── ...            # Other Django files
        └── Doc/
            ├── 3_Postman_API_Collection.rtf
            ├── Project_Full_code_Part_1.rtf
            └── Project_Full_code_Part_2.rtf
```

---

## Local Media Storage

- Files uploaded are stored locally under `/media/` directory (for development).
- You can change storage backend in Django settings.

---

## License

MIT License. See [LICENSE](LICENSE).

---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

---

## Author

Ranjith Kumar (@sairanjith101)

---

## Support

If you face any issues, check the API docs, Postman collection, or open a GitHub issue.
