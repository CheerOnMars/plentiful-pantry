# plentiful-pantry

Uses Python 3.7.0

Uses Flask
  - $ python3 -m venv venv (create virtual environment)
  - $ source venv/bin/activate (activate virtual environment)
  - (venv) $ pip install flask (install flask)
  - (venv) $ export FLASK_APP=plentiful_pantry.py
  - (venv) $ flask run

Flask-SQLAlchemy,
  - (venv) $ pip install flask-sqlalchemy
  - (venv) $ pip install flask-migrate

Flask-WTF
  - (venv) $ pip install flask-wtf

psycopg2 2.6.1
  - pip install psycopg2

Sqlalchemy Seeder
  - pip install sqlalchemy-seeder

Requests module
  - pip install requests

Beautiful Soup
  - pip install beautifulsoup4

Heroku
 - heroku apps:create plentiful-pantry

Heroku Postgres Database
 - heroku addons:add heroku-postgresql:hobby-dev
 - URL for the newly created database is stored in a DATABASE_URL environment variable
 - heroku config:set LOG_TO_STDOUT=1
 - heroku addons:create searchbox:starter

Requirements
- pip freeze > requirements.txt
- pip install -r requirements.txt

Procfile
  - heroku config:set FLASK_APP=plentiful_pantry.py

