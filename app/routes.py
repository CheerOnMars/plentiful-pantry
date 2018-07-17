import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category

# import pdb; pdb.set_trace()

import json
with open('data/recipes.json') as f:
    json_recipes_struct = json.load(f)

import csv
with open('data/ingredients.csv', 'r') as f:
    reader = csv.reader(f)
    csv_ingredients_struct = list(reader)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Super Sario'}
    return render_template('index.html', title='Home', user=user, recipes=json_recipes_struct)

@app.route('/ingredients')
def ingredients():
    user = {'username': 'Super Sario'}
    return render_template('ingredient_list.html', title='Ingredients', user=user, ingredients=csv_ingredients_struct)

@app.route('/recipes')
def recipes():
    user = {'username': 'Super Sario'}
    recipes = Recipe.query.order_by(Recipe.name.asc())
    return render_template('recipes.html', title='Recipes', user=user, recipes=recipes)
