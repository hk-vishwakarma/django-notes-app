#  Django Notes App

A simple and secure Notes application built with **Django**.  
Users can **register, log in, add notes, view all notes, and manage personal notes** in one place.  

---

##  Features
-  User registration & login (authentication system)
-  Create, read, update, and delete notes
-  User-specific notes (each user sees only their own notes)
-  Responsive and clean UI
-  Secure with Django’s authentication

---

##  Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap)
- **Database:** SQLite (default, can be replaced with PostgreSQL/MySQL)
- **Authentication:** Django’s built-in auth system

---

##  Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-notes-app.git
cd django-notes-app

### 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Set Up Database
python manage.py makemigrations
python manage.py migrate


### 5. Create Superuser (optional, for admin access)
python manage.py createsuperuser


### 6. Run the Server
python manage.py runserver
Visit  http://127.0.0.1:8000 in your browser.


## Screenshots

### Homepage
![Homepage](screenshots/home.jpg)

### Home Page After Login
![Home Page](screenshots/home after login.jpg)

### Login Page
![Login Page](screenshots/login.jpg)

### Sign Up Page
![Signup Page](screenshots/Sign_up.jpg)

### Add Note Page
![Add Note Page](screenshots/Addnote.jpg)

### Success Page
![Success Page](screenshots/Success msg page.jpg)

### All Note Page
![All Note Page](screenshots/all note.jpg)

### View Full Note Page
![View full note Page](screenshots/View full note page.jpg)


## Project Structure
django-notes-app/
│── notes/                # App folder
│── projectname/          # Project folder
│── templates/            # HTML templates
│── static/               # CSS, JS, images
│── screenshots/          # App screenshots
│── db.sqlite3            # Database file
│── manage.py
│── requirements.txt
│── README.md


## Author
Hemant Kumar Vishwakarma
