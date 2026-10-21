**Author:** Muhsin
# Day 7 – Django Clean Architecture

A Django project demonstrating clean structure, environment config, and Git workflow.

## Setup (Windows PowerShell)
```powershell
git clone <repo-url>
cd day7_project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env     # then edit .env with a real SECRET_KEY
python manage.py migrate
python manage.py runserver
```

## Generate a secret key
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Project Structure
- `config/` – settings and root URLs
- `apps/` – Django apps (business features)
  - `apps/tasks/services.py` – business logic (views stay thin)
- `core/` – shared constants and exceptions
- `utils/` – small helper functions

## API
- `GET /api/tasks/` – list tasks
- `GET /api/tasks/<id>/` – task detail

## Environment Variables
See `.env.example`.
