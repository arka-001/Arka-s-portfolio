# Arka Portfolio - Full Stack Portfolio Website

A complete portfolio website built with Django REST Framework backend and MySQL database, featuring a comprehensive admin panel for content management.

## 🚀 Features

### Backend Features
- **Django REST Framework API** - Complete REST API for all portfolio data
- **MySQL Database** - Robust database with comprehensive schema
- **Admin Panel** - Full-featured Django admin for content management
- **Image/File Upload** - Support for profile images, project screenshots, and documents
- **CORS Support** - Ready for frontend integration
- **Pagination** - API pagination for better performance

### Portfolio Sections
- **About** - Personal information and social links
- **Skills** - Technical skills with proficiency levels and categories
- **Projects** - Portfolio projects with technologies and links
- **Experience** - Work history and professional experience
- **Education** - Academic background and qualifications
- **Services** - Services offered with icons and descriptions
- **Testimonials** - Client testimonials and reviews
- **Blog** - Blog posts with categories and tags
- **Contact** - Contact form for inquiries

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5, Django REST Framework 3.16.1
- **Database**: MySQL
- **Image Processing**: Pillow
- **CORS**: django-cors-headers
- **Python**: 3.13+

## 📋 Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd arka-portfolio
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. Create MySQL database:
```sql
CREATE DATABASE arka_portfolio;
```

2. Update database settings in `arka_portfolio/settings.py` if needed:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arka_portfolio',
        'USER': 'root',
        'PASSWORD': 'Arka',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Populate Sample Data (Optional)
```bash
python manage.py populate_sample_data
```

### 8. Run Development Server
```bash
python manage.py runserver
```

## 🌐 Access Points

- **Admin Panel**: http://localhost:8000/admin/
- **API Root**: http://localhost:8000/api/
- **API Documentation**: http://localhost:8000/api/

## 📚 API Endpoints

### Available Endpoints
- `GET /api/about/` - Get personal information
- `GET /api/skills/` - Get skills list
- `GET /api/projects/` - Get projects list
- `GET /api/experience/` - Get work experience
- `GET /api/education/` - Get education history
- `POST /api/contact/` - Submit contact form
- `GET /api/blog/` - Get blog posts
- `GET /api/testimonials/` - Get testimonials
- `GET /api/services/` - Get services offered

### Query Parameters
- **Skills**: `?category=programming` - Filter by skill category
- **Projects**: `?featured=true&type=web` - Filter featured projects by type
- **Blog**: `?search=django&featured=true` - Search and filter blog posts

### Example API Usage
```bash
# Get all skills
curl http://localhost:8000/api/skills/

# Get featured projects
curl http://localhost:8000/api/projects/?featured=true

# Get programming skills
curl http://localhost:8000/api/skills/?category=programming

# Submit contact form
curl -X POST http://localhost:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","subject":"Inquiry","message":"Hello!"}'
```

## 🎨 Admin Panel Features

### Dashboard Overview
- **Arka Portfolio Admin** - Custom admin branding
- **Comprehensive Management** - All portfolio sections manageable
- **Bulk Actions** - Mark messages as read/unread, publish/unpublish posts
- **Advanced Filtering** - Filter by status, dates, categories
- **Inline Editing** - Quick edit capabilities for lists
- **Media Management** - Upload and manage images/files

### Content Management
- **About Section** - Personal info, social links, resume upload
- **Skills Management** - Add skills with proficiency levels and colors
- **Project Portfolio** - Create projects with technologies and links
- **Experience Timeline** - Manage work history and company logos
- **Education Records** - Academic background and institution logos
- **Service Offerings** - Define services with icons and descriptions
- **Client Testimonials** - Manage testimonials with ratings
- **Blog Management** - Create and publish blog posts
- **Contact Management** - View and manage contact form submissions

## 📁 Project Structure

```
arka-portfolio/
├── arka_portfolio/          # Django project settings
│   ├── settings.py         # Main settings file
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── portfolio/              # Main portfolio app
│   ├── models.py          # Database models
│   ├── views.py           # API views
│   ├── serializers.py     # API serializers
│   ├── admin.py           # Admin panel configuration
│   ├── urls.py            # App URL patterns
│   └── management/        # Custom management commands
├── frontend/              # Frontend files (your existing frontend)
├── static/                # Static files
├── media/                 # Uploaded media files
├── manage.py              # Django management script
└── README.md              # This file
```

## 🔒 Security Features

- **CORS Configuration** - Properly configured for frontend integration
- **Input Validation** - Comprehensive form validation
- **File Upload Security** - Secure file upload handling
- **Admin Authentication** - Secure admin panel access

## 🚀 Deployment

### Production Setup
1. Set `DEBUG = False` in settings.py
2. Configure production database
3. Set up static file serving
4. Configure environment variables
5. Set up web server (nginx + gunicorn)

### Environment Variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=mysql://user:password@host:port/database
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 📞 Support

For support and questions:
- Email: arkamaitra001@gmail.com
- 

---

**Built with ❤️ by Arka Maitra**
