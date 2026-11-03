# TalentBridge (Django)

First time (inside your activated venv, in this folder):

    python -m pip install -r requirements.txt
    python manage.py createsuperuser
    python manage.py runserver

`runserver` creates the database tables automatically (migrations are included).
Admin: http://127.0.0.1:8000/admin/ - add Jobs and Posts there; form messages arrive under Leads.
