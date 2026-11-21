# StateSpaces Prototype

Quick Django prototype for StateSpaces

## Setup

```bash
git clone https://github.com/yw-blp/statespaces-prototype.git
cd statespaces-prototype
```

# Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate        # For Windows
source .venv/bin/activate     # For macOS/Linux
```

# Install Dependencies

```bash
pip install -r requirements.txt
```

## Setup Local Database

As 'db.sqlite3' is in '.gitignore', each person creates their own local database 

```bash
python manage.py migrate
python manage.py createsuperuser
```

# Run

```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000 (or http://127.0.0.1:8000/admin for admin page)

## Structure

- config/ contains the project settings and the root URL config
- statespaces/ is the main app (models, views, templates)
