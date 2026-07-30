# Todo App — Django Project

A full-stack task management web application built with Django, allowing users to create, view, edit, and delete daily tasks through a clean, styled interface.

## Features

- **Create tasks** with a title, description, and completion status
- **View all tasks** in a clean, organized table with serial numbers
- **Edit existing tasks** using a pre-filled form
- **Delete tasks** with a confirmation prompt to prevent accidental removal
- **Status badges** — green "Completed" and yellow "Pending" indicators
- **Form validation** — task titles must be at least 3 characters long
- **Admin dashboard** — manage tasks directly through Django's built-in admin panel, with search and filter support

## Tech Stack

- **Backend:** Python 3.14, Django 6.0
- **Database:** SQLite (development)
- **Frontend:** Django Templates, Bootstrap 5
- **Version Control:** Git & GitHub

## Project Structure

ALL_ABOUT_DJANGO/
├── tasks/              # Main app: models, views, forms, templates
├── todo_project/       # Project settings and URL configuration
├── manage.py
└── requirements.txt

## Setup Instructions

1. Clone the repository:

git clone <repository-url>

2. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run migrations:

python manage.py migrate

5. Start the development server:

python manage.py runserver

6. Visit `http://127.0.0.1:8000` in your browser.

## What I Learned

This project was built as part of a structured Django curriculum, covering:
- Project setup and virtual environments
- URL routing and function-based views
- Template inheritance with the Django Template Language
- Models, migrations, and the Django ORM
- The Django admin interface
- Forms, validation, and full CRUD operations
- UI styling with Bootstrap

## Author

Morita — TechRise Django Curriculum