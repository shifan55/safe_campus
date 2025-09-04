# StopRagging – Role-based Django Starter

Features:
- Separate apps for Administrator, Counselor, Student
- Google OAuth (django-allauth) pre-wired
- Anonymous & authenticated reporting with Google Maps location tagging
- Admin & Counselor dashboards (Chart.js in Admin)
- Bootstrap UI (reuses your existing templates where possible)
- SQLite default; env-driven secrets

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill keys
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Then open http://127.0.0.1:8000/
