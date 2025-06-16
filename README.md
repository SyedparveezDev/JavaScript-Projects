# 📈 IPO Web Application

An IPO (Initial Public Offering) Web App built for Bluestock Fintech as part of an internship project. It provides detailed IPO listings, a secure admin dashboard, and public-facing APIs — all powered by Django and PostgreSQL.

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tech Stack](https://img.shields.io/badge/stack-Django%20%7C%20PostgreSQL%20%7C%20Bootstrap-blue)

---

## 🚀 Live Demo

> The development server is now running with a basic preview at [http://localhost:8000](http://localhost:8000)

---

## 📌 Features

### 🔍 Public User Interface

- List IPOs (Upcoming, Ongoing, Listed)
- IPO Detail Page with comprehensive information
- RHP & DRHP PDF Downloads
- Search and Filter by Name/Status
- Responsive Bootstrap design

### 🔐 Admin Panel

- Django Admin interface
- Login-secured Dashboard
- Create, Update, Delete IPOs
- Upload RHP/DRHP PDFs & Company Logos
- User management

### 📡 RESTful API

- `GET /api/` → API Overview
- `GET /api/ipo/` → All IPOs with filtering and search
- `GET /api/ipo/<id>/` → IPO Detail
- Search, Filter & Sort supported
- JSON responses with pagination

---

## 🛠️ Project Structure

```
ipo-web-app/
├── ipo_project/          # Main Django project
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI application
│   └── asgi.py          # ASGI application
├── ipo_app/             # IPO Django app
│   ├── models.py        # IPO model
│   ├── views.py         # Web and API views
│   ├── admin.py         # Admin configuration
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # App URL patterns
│   └── tests.py         # Test cases
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   └── ipo_app/         # App-specific templates
├── static/              # Static files
│   └── css/             # Custom CSS
├── media/               # User uploaded files
├── requirements.txt     # Python dependencies
├── manage.py           # Django management script
└── simple_server.py    # Development server
```

---

## 🧠 Prerequisites

- Python 3.8+
- PostgreSQL (for production)
- Git
- Virtual environment (recommended)

---

## ⚙️ Tech Stack

| Layer     | Technology                   |
| --------- | ---------------------------- |
| Backend   | Python 3.12, Django 5.0.6    |
| REST API  | Django REST Framework 3.15.1 |
| Database  | PostgreSQL / SQLite          |
| Frontend  | HTML5, CSS3, JavaScript      |
| UI Design | Bootstrap 5.3.0              |
| Tools     | Git, Django Admin            |

---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/ipo-web-app.git
cd ipo-web-app
```

### 2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Environment Configuration**

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=ipo_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. **Database Setup**

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py loaddata sample_data.json
```

### 6. **Run Development Server**

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) to see the application.

---

## 📱 Usage

### Web Interface

1. **Home Page** - Overview of featured IPOs
2. **IPO Listings** - Browse all IPOs with filters
3. **IPO Details** - Detailed view with documents
4. **Admin Panel** - Manage IPOs at `/admin/`

### API Endpoints

```bash
# Get all IPOs
curl http://localhost:8000/api/ipo/

# Get specific IPO
curl http://localhost:8000/api/ipo/1/

# Filter by status
curl http://localhost:8000/api/ipo/?status=upcoming

# Search by company name
curl http://localhost:8000/api/ipo/?search=company
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test ipo_app

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 🚀 Deployment

### Production Settings

1. Set `DEBUG=False` in production
2. Configure PostgreSQL database
3. Set up static file serving
4. Use Gunicorn as WSGI server

```bash
# Install production dependencies
pip install gunicorn psycopg2-binary

# Collect static files
python manage.py collectstatic

# Run with Gunicorn
gunicorn ipo_project.wsgi:application
```

---

## 📊 API Documentation

### IPO Model Fields

- `company_name` - Company name (string)
- `company_logo` - Company logo image (file)
- `issue_size` - Issue size in crores (decimal)
- `price_band` - Price range (string)
- `open_date` - IPO opening date (date)
- `close_date` - IPO closing date (date)
- `listing_date` - Stock listing date (date, optional)
- `status` - IPO status (upcoming/ongoing/listed)
- `rhp_document` - RHP document (file)
- `drhp_document` - DRHP document (file)
- `description` - Company description (text)
- `lot_size` - Minimum lot size (integer)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎯 Development Status

✅ **Completed Features:**

- Django project structure
- IPO model and admin
- Web interface with Bootstrap
- REST API with DRF
- Search and filtering
- File upload functionality
- Responsive design
- Test suite

🚧 **In Progress:**

- Production deployment
- Advanced analytics
- User authentication
- Email notifications

📋 **Future Enhancements:**

- Real-time updates
- Mobile app
- Payment integration
- Advanced reporting

---

## 📞 Support

For support and questions:

- Create an issue on GitHub
- Contact: [your-email@example.com]
- Documentation: [Project Wiki]

---

_Built with ❤️ for Bluestock Fintech_
