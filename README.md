## QR Code Generator API
I needed a QR Code for my cat's vet last week. I found a website for code generating and I did use it. There are sent me an email about my generated code and why it is canceled.

There are want a package from me and it is so expensive in my country. I thought about it, how can I generate a completely free QR Code? I researched it and I did.

QR Code Generator API is written in Python/Django and Django Rest Framework. I started developing the app on Sunday.

I have a little TODO list for other versions and after I will complete the app with React App.

**Todo List:**
- Add different data types like rgb and rgba codes for gradient QR Code generating.
- Add update endpoint for created QR Codes and re-generate qr code function.
- Create a React App
    - Login Page
    - Register Page
    - Profile Page, Update Password and Change Email features
    - Generate QR Code Page
    - List Codes Page
    - Update Generate Code Page

## Requirements
- Python 3.x
- PostgreSQL

## How to install
Create an virtual environment:
```shell
python -m venv venv
or
virtualenv venv
```

Install the pip packages:
```shell
pip install -r requirements.txt
```

Create an environment file with the name `.env` like:
```text
DEBUG=True
SECRET_KEY=secret_key
HOST=localhost
USER=postgres
PASSWORD=12345
NAME=qrcode
PORT=5432
```

## Authentication
I use TokenAuthentication for API endpoints. If you want to use QR Code Generator API, you must have a user account. You can create a user account with the register endpoint and you can get an authentication token with the login endpoint.

## Endpoints
```HTTP
// Register
POST http://localhost:8000/api/v1/register/
Content-Type: application/json

{
    "username": "ziyacivan",
    "password": "123456",
    "email": "yusufziyacivan@gmail.com"
}

// Login
POST http://localhost:8000/api/v1/login/
Content-Type: application/json

{
    "username": "ziyacivan",
    "password": "123456"
}

// Logout
POST http://localhost:8000/api/v1/logout/
Content-Type: application/json
Authorization: Token b550062d5fc3b81dda4c8287424c6bc0f8e6d5cb

// Profile
GET http://localhost:8000/api/v1/profile/
Content-Type: application/json
Authorization: Token b550062d5fc3b81dda4c8287424c6bc0f8e6d5cb

// Generate Code
POST http://localhost:8000/api/v1/qrcodes/generate/
Content-Type: application/json
Authorization: Token b550062d5fc3b81dda4c8287424c6bc0f8e6d5cb

{
    "name": "QRCode Generator",
    "description": "This is a QRCode generator app",
    "url": "https://github.com/ziyacivan/qrcode-generator-api"
}

// QR Code List
GET http://localhost:8000/api/v1/qrcodes/
Content-Type: application/json
Authorization: Token b550062d5fc3b81dda4c8287424c6bc0f8e6d5cb

// QR Code Detail
GET http://localhost:8000/api/v1/qrcodes/4/
Content-Type: application/json
Authorization: Token b550062d5fc3b81dda4c8287424c6bc0f8e6d5cb
```
