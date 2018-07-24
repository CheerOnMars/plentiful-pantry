import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from app.forms import InventoryForm, EditRecipeForm

# import pdb; pdb.set_trace()

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Super Sario'}
    recipes = Recipe.query.order_by(Recipe.name.asc())
    condiments = Recipe.query.filter_by(category='Condiment')
    mains = Recipe.query.filter_by(category='Main course')
    drinks = Recipe.query.filter_by(category='Drink')
    sandwiches = Recipe.query.filter_by(category='Sandwich')
    breads = Recipe.query.filter_by(category='Bread / pastry')
    salads = Recipe.query.filter_by(category='Salad')
    desserts = Recipe.query.filter_by(category='Dessert')
    snacks = Recipe.query.filter_by(category='Snack')
    sides = Recipe.query.filter_by(category='Side dish')
    appetizers = Recipe.query.filter_by(category='Appetizer')
    soups = Recipe.query.filter_by(category='Soup')
    rec_dict = {condiments: 'Condiments', mains: 'Main courses', drinks: 'Drinks', sandwiches: 'Sandwiches', breads: 'Breads', salads: 'Salads', desserts: 'Desserts', snacks: 'Snacks', desserts: 'Dessert', snacks: 'Snacks', sides: 'Sides', appetizers: 'Appetizers', soups: 'Soup'}
    return render_template('index.html', title='Home', user=user, recipes=recipes, condiments=condiments, mains=mains, drinks=drinks, sandwiches=sandwiches, breads=breads, salads=salads, desserts=desserts, snacks=snacks, sides=sides, appetizers=appetizers, soups=soups, rec_dict=rec_dict)

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
    recipe_ingredients = recipe.ingredients
    inventory = Inventory.query.all()
    return render_template('recipe.html', title='Recipe', user=user, recipe=recipe, recipe_ingredients=recipe_ingredients, inventory=inventory)

@app.route('/inventory', methods=['GET', 'POST'])
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
    cat_dict = {produce: 'Produce', dairy: 'Dairy', eggs: 'Eggs', meat: 'Meat',
        condiments: 'Condiments', spices: 'Spices', nuts: 'Nuts',
        beverages: 'Beverages', oils: 'Oils/Vinegars', grains: 'Grains',
        beans: "Beans", baking: 'Baking', dessert:'Dessert', misc: 'Misc'}

    form = InventoryForm()
    if form.validate_on_submit():
        flash('Inventory updated'.format())
        # item = Inventory.query.filter_by(id=id).first_or_404()
        # item = Inventory(id=form.id.data)
        # item.is_present = form.is_present.data
        # db.session.commit()
        return redirect(url_for('index'))
    return render_template('inventory.html', title='Inventory', form=form,
        inventory=inventory, produce=produce, dairy=dairy, eggs=eggs, meat=meat,
        condiments=condiments, spices=spices, nuts=nuts, beverages=beverages,
        oils=oils, grains=grains, beans=beans, baking=baking, dessert=dessert,
        misc=misc, cat_dict= cat_dict)

@app.route('/edit_recipe/<id>', methods=['GET', 'POST'])
def edit_recipe(id):
    recipe = Recipe.query.get(id)
    recipe_ingredients = recipe.ingredients
    form = EditRecipeForm()
    if form.validate_on_submit():
        recipe.name = form.name.data
        recipe.description = form.description.data
        recipe.recipe_yield = form.recipe_yield.data
        recipe.category = form.category.data
        recipe.image = form.image.data
        recipe.source = form.source.data
        recipe.url = form.url.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('recipe', id=recipe.id))
    elif request.method == 'GET':
        form.name.data = recipe.name
        form.description.data = recipe.description
        form.recipe_yield.data = recipe.recipe_yield
        form.category.data = recipe.category
        form.image.data = recipe.image
        form.source.data = recipe.source
        form.url.data = recipe.url
    return render_template('edit_recipe.html', title='Edit Recipe', form=form,
        recipe=recipe, recipe_ingredients=recipe_ingredients)

@app.route('/')
@app.route('/options')
def options():
    user = {'username': 'Super Sario'}
    recipes = Recipe.query.order_by(Recipe.name.asc())
    condiments = Recipe.query.filter_by(category='Condiment')
    mains = Recipe.query.filter_by(category='Main course')
    drinks = Recipe.query.filter_by(category='Drink')
    sandwiches = Recipe.query.filter_by(category='Sandwich')
    breads = Recipe.query.filter_by(category='Bread / pastry')
    salads = Recipe.query.filter_by(category='Salad')
    desserts = Recipe.query.filter_by(category='Dessert')
    snacks = Recipe.query.filter_by(category='Snack')
    sides = Recipe.query.filter_by(category='Side dish')
    appetizers = Recipe.query.filter_by(category='Appetizer')
    soups = Recipe.query.filter_by(category='Soup')
    rec_dict = {condiments: 'Condiments', mains: 'Main courses', drinks: 'Drinks', sandwiches: 'Sandwiches', breads: 'Breads', salads: 'Salads', desserts: 'Desserts', snacks: 'Snacks', desserts: 'Dessert', snacks: 'Snacks', sides: 'Sides', appetizers: 'Appetizers', soups: 'Soup'}
    return render_template('options.html', title='Options', user=user, recipes=recipes, condiments=condiments, mains=mains, drinks=drinks, sandwiches=sandwiches, breads=breads, salads=salads, desserts=desserts, snacks=snacks, sides=sides, appetizers=appetizers, soups=soups, rec_dict=rec_dict)
