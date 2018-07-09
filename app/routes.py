from flask import render_template
from app import app

import json
with open('data/recipes.json') as f:
    recipes_struct = json.load(f)

import csv
with open('data/ingredients.csv', 'r') as f:
    reader = csv.reader(f)
    ingredients_struct = list(reader)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Super Sario'}
    return render_template('index.html', title='Home', user=user, recipes=recipes_struct)

@app.route('/inventory')
def inventory():
    user = {'username': 'Super Sario'}
    return render_template('inventory.html', title='Home', user=user, ingredients=ingredients_struct)
