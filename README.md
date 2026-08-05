# Todo App — Django Project

A full-stack task management web application built with Django, allowing users to create, view, edit, and delete daily tasks through a clean, styled interface.

[Live Demo](https://todo-app-9h91.onrender.com)

---

## Features

- **User Authentication:** Secure signup, login, and user session management.
- **Task Management:** Full CRUD operations (Create, Read, Update, Delete) for daily tasks.
- **Visual Status Badges:** Green "Completed" and yellow "Pending" indicators.
- **Form Validation:** Client-side and server-side validation for form submissions.
- **Admin Dashboard:** Built-in Django admin interface with search and filter support.

---

## Tech Stack

- **Backend:** Python 3, Django
- **Database:** PostgreSQL (Production on Render), SQLite (Local Development)
- **Frontend:** Django Templates, Bootstrap 5
- **Deployment:** Render
- **Version Control:** Git & GitHub

---

## Project Structure

```text
django-todo-app/
├── todo_list/          # Project settings and root URL routing
├── tasks/              # Main application logic (models, views, forms, templates)
├── manage.py
├── requirements.txt
└── build.sh            # Render build script

## Setup Instructions

1. Clone the repository:

git clone https://github.com/CrystalViiva/django-todo-app.git
cd django-todo-app

2. Create and activate a virtual environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Run migrations:

python manage.py migrate

5. Start the development server:

python manage.py runserver

6. Visit `http://127.0.0.1:8000` in your browser.

## What I Learned

This project was built as part of the TechRise Django curriculum, covering:

- Virtual environments, environment security (.env), and dynamic configuration parsing (ALLOWED_HOSTS).

- Function-based views, URL routing, and Django Template Language (DTL).

- Relational data modeling with Django ORM and PostgreSQL integration.

- Full CRUD operations, forms, and custom validation logic.

- Production deployment and web service management on Render.

## Author

Vivian Njoku — TechRise Django Curriculum