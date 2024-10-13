# Next-Gen-AI-Writing-APP

This is a full-stack application consisting of an Angular frontend and a Django backend designed for an AI-powered writing experience.

Table of Contents
Prerequisites
Backend Setup
Frontend Setup
Running the Application
API Endpoints
Contributing
License
Prerequisites
Before you begin, ensure you have the following installed:

Node.js (version >= 14.x)
Angular CLI (version >= 12.x)
Python (version >= 3.6)
pip (Python package installer)
virtualenv (optional but recommended)
Backend Setup (Django)
Clone the Backend Repository

bash
Copy code
git clone https://github.com/saadali2425/Next-Gen-AI-Writing-APP.git
cd Next-Gen-AI-Writing-APP
Create a Virtual Environment (Optional)

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `.\env\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run Migrations

bash
Copy code
python manage.py migrate
Create a Superuser (Optional)

bash
Copy code
python manage.py createsuperuser
Start the Django Development Server

bash
Copy code
python manage.py runserver
The backend should now be running at http://127.0.0.1:8000/.