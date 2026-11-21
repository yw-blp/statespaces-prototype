## Setup

git clone https://github.com/yw-blp/statespaces-prototype.git
cd statespaces-prototype

# Virtual Environment
python -m venv .venv			# For Windows
source .venv/bin/activate		# For macOS or Linux

# Install Dependencies
pip install -r requirements.txt

## As db.sqlite3 is in gitignore, setup local database
python manage.py migrate
python manage.py createsuperuser

# Run
python manage.py runserver
Open http://127.0.0.1:8000

## Structure
- config/ contains the project settings and the root URL config
- statespaces/ is the main app (models, views, templates)