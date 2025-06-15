# 📈 IPO Web Application

An IPO (Initial Public Offering) Web App built for Bluestock Fintech as part of an internship project. It provides detailed IPO listings, a secure admin dashboard, and public-facing APIs — all powered by Django and PostgreSQL.

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tech Stack](https://img.shields.io/badge/stack-Django%20%7C%20PostgreSQL%20%7C%20Bootstrap-blue)

---

## 🚀 Live Demo

> Coming Soon — [Bluestock Production URL](https://bluestock.in/)

---

## 📌 Features

### 🔍 Public User Interface

- List IPOs (Upcoming, Ongoing, Listed)
- IPO Detail Page
- RHP & DRHP PDF Downloads
- Search and Filter by Name/Status

### 🔐 Admin Panel

- Login-secured Dashboard
- Create, Update, Delete IPOs
- Upload RHP/DRHP PDFs & Logos

### 📡 RESTful API

- `GET /api/ipo/` → All IPOs
- `GET /api/ipo/<id>/` → IPO Detail
- Search, Filter & Sort supported

---

## 🧠 Prerequisites

- Python 3.12+
- PostgreSQL
- Git, VS Code
- Django & DRF Libraries

---

## ⚙️ Tech Stack

| Layer      | Tech                        |
|------------|-----------------------------|
| Backend    | Python, Django 5.0.6         |
| REST API   | Django REST Framework 3.15.1 |
| Database   | PostgreSQL                  |
| Frontend   | HTML, CSS, JavaScript        |
| UI Design  | Bootstrap 5 (CDN)            |
| Tools      | Postman, GitHub              |

---

## 🛠️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/ipo-web-app.git
   cd ipo-web-app
