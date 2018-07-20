import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from app.forms import InventoryForm

# import pdb; pdb.set_trace()

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Super Sario'}
    recipes = Recipe.query.order_by(Recipe.name.asc())
    return render_template('index.html', title='Home', user=user, recipes=recipes)

@app.route('/ingredients')
def ingredients():
    user = {'username': 'Super Sario'}
    ingredients = Ingredient.query.order_by(Ingredient.name.asc())
    return render_template('ingredient_list.html', title='Ingredients', user=user, ingredients=ingredients)

@app.route('/recipes')
def recipes():
    user = {'username': 'Super Sario'}
    recipes = Recipe.query.order_by(Recipe.name.asc())
    return render_template('recipes.html', title='Recipes', user=user, recipes=recipes)

@app.route('/recipe/<id>')
def recipe(id):
    user = {'username': 'Super Sario'}
    recipe = Recipe.query.get(id)
    return render_template('recipe.html', title='Recipe', user=user, recipe=recipe)

@app.route('/inventory')
def inventory():
    ingredients = Ingredient.query.order_by(Ingredient.name.asc())
    form = InventoryForm()
    return render_template('inventory.html', title='Inventory', form=form, ingredients=ingredients)
