from flask import render_template
from app import app

import json
with open('data/recipes.json') as f:
    recipes_struct = json.load(f)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Super Sario'}
    return render_template('index.html', title='Home', user=user, recipes=recipes_struct)
