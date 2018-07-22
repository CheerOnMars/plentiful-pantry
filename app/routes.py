import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from app.forms import InventoryForm, RecipeForm

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
    recipe_ingredients = RecipeIngredient.query.all()
    ingredients = Ingredient.query.all()
    return render_template('recipes.html', title='Recipes', user=user, recipes=recipes, ingredients=ingredients, recipe_ingredients=recipe_ingredients)

@app.route('/recipe/<id>')
def recipe(id):
    user = {'username': 'Super Sario'}
    recipe = Recipe.query.get(id)
    rec_ingredients = recipe.ingredients
    return render_template('recipe.html', title='Recipe', user=user, recipe=recipe, rec_ingredients=rec_ingredients)

@app.route('/inventory')
def inventory():
    # ingredients = Ingredient.query.order_by(Ingredient.name.asc())
    inventory = Inventory.query.all()
    produce = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Produce')
    dairy = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Dairy/Dairy Substitutes')
    eggs = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Eggs')
    meat = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Meat/Fish')
    condiments = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Condiments')
    spices = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Spices')
    nuts = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Nuts')
    beverages = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Beverage')
    oils = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Oils/Vinegars')
    grains = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Grains')
    beans = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Beans')
    baking = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Baking')
    dessert = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Dessert')
    misc = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == 'Misc')
    categories = [produce, dairy, eggs, meat, condiments, spices, nuts, beverages, oils, grains, beans, baking, dessert, misc]
    form = InventoryForm()
    if form.validate_on_submit():
        flash('Inventory updated'.format())
        return redirect('/index')
    return render_template('inventory.html', title='Inventory', form=form, inventory=inventory, produce=produce, dairy=dairy, eggs=eggs, meat=meat, condiments=condiments, spices=spices, nuts=nuts, beverages=beverages, oils=oils, grains=grains, beans=beans, baking=baking, dessert=dessert, misc=misc, categories=categories)
