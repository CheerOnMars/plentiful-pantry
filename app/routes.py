"""
This module will provide RESTful endpoints for all requests
necessary to fulfill the requirements.
"""
from flask import render_template, flash, redirect, url_for
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

@app.route('/ingredients')
def ingredients():
    user = {'username': 'Super Sario'}
    return render_template('ingredient_list.html', title='Home', user=user, ingredients=ingredients_struct)
