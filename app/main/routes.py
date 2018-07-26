from flask import render_template, flash, redirect, url_for, request, current_app
from app import db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from app.main.forms import EditRecipeForm, EditInventoryForm
from app.main import bp



# import pdb; pdb.set_trace()

@bp.route('/recipes/<category>')
def home(category):
    user = {'username': 'Super Sario'}
    rec_cat_dict = { 'mains': 'Main course', 'sides': 'Side dish', 'salads': 'Salad', 'soups': 'Soup', 'appetizers': 'Appetizer', 'sandwiches': 'Sandwich', 'breads': 'Bread / pastry', 'snacks': 'Snack', 'desserts': 'Dessert', 'drinks': 'Drink', 'condiments': 'Condiment', 'all': 'all'}
    categories = Category.query.order_by(Category.name.asc())
    if category == 'all':
        recipes = Recipe.query.order_by(Recipe.name.asc())
    else:
        recipes = Recipe.query.filter_by(category=rec_cat_dict[category])
    return render_template('recipes_category.html', title='Recipes', categories=categories, user=user, recipes=recipes, category=category, rec_cat_dict=rec_cat_dict)


@bp.route('/index')
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
    rec_dict = { mains: 'Main course', sides: 'Side dish', salads: 'Salad', soups: 'Soup', appetizers: 'Appetizer', sandwiches: 'Sandwich', breads: 'Bread / pastry', snacks: 'Snack', desserts: 'Dessert', drinks: 'Drink', condiments: 'Condiment'}
    return render_template('index.html', title='Index', user=user, recipes=recipes, condiments=condiments, mains=mains, drinks=drinks, sandwiches=sandwiches, breads=breads, salads=salads, desserts=desserts, snacks=snacks, sides=sides, appetizers=appetizers, soups=soups, rec_dict=rec_dict)


@bp.route('/recipe/<id>')
def recipe(id):
    user = {'username': 'Super Sario'}
    recipe = Recipe.query.get(id)
    recipe_ingredients = recipe.ingredients
    inventory = Inventory.query.all()
    return render_template('recipe.html', title='Recipe', user=user, recipe=recipe, recipe_ingredients=recipe_ingredients, inventory=inventory)


@bp.route('/edit_recipe/<id>', methods=['GET', 'POST'])
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
        return redirect(url_for('main.recipe', id=recipe.id))
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


@bp.route('/inventory')
def inventory():
    ingredients = Ingredient.query.all()
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
    cat_dict = {produce: 'Produce', dairy: 'Dairy', eggs: 'Eggs', meat: 'Meat', condiments: 'Condiments', spices: 'Spices', nuts: 'Nuts', beverages: 'Beverages', oils: 'Oils/Vinegars', grains: 'Grains', beans: "Beans", baking: 'Baking', dessert:'Dessert', misc: 'Misc'}

    return render_template('inventory.html', title='Inventory', inventory=inventory, produce=produce, dairy=dairy, eggs=eggs, meat=meat, condiments=condiments, spices=spices, nuts=nuts, beverages=beverages, oils=oils, grains=grains, beans=beans, baking=baking, dessert=dessert, misc=misc, cat_dict= cat_dict)



@bp.route('/options')
def options():
    user = {'username': 'Super Sario'}
    all_recipes = Recipe.query.order_by(Recipe.name.asc())
    my_recipes = Recipe.find_options(all_recipes)
    categories = Category.query.order_by(Category.name.asc())
    flip_rec_dict = { "Main course": "mains", "Side dish": "sides", "Salad": "salads", "Soup": "soups", "Appetizer": "appetizers", "Sandwich": "sandwiches", "Bread / pastry": "breads", "Snack": "snacks", "Dessert": "desserts", "Drink": "drinks", "Condiment": "condiments"}

    return render_template('options.html', title='Options', user=user, my_recipes=my_recipes, categories=categories, flip_rec_dict=flip_rec_dict)


@bp.route('/options_category/<rec_category>')
def options_category(rec_category):
    user = {'username': 'Super Sario'}
    cat_recipes = Recipe.query.filter_by(category=str(rec_category))
    all_recipes = Recipe.query.order_by(Recipe.name.asc())
    my_cat_recipes = Recipe.find_options(cat_recipes)
    categories = Category.query.order_by(Category.name.asc())
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
    flip_rec_dict = { "Main course": "mains", "Side dish": "sides", "Salad": "salads", "Soup": "soups", "Appetizer": "appetizers", "Sandwich": "sandwiches", "Bread / pastry": "breads", "Snack": "snacks", "Dessert": "desserts", "Drink": "drinks", "Condiment": "condiments"}

    return render_template('options_category.html', title='Option Category', user=user, my_cat_recipes=my_cat_recipes, rec_category=rec_category, categories=categories, flip_rec_dict=flip_rec_dict, recipes=recipes, condiments=condiments, mains=mains, drinks=drinks, sandwiches=sandwiches, breads=breads, salads=salads, desserts=desserts, snacks=snacks, sides=sides, appetizers=appetizers, soups=soups)


@bp.route('/inventory/toggle/<id>', methods=['GET', 'POST'])
def toggle_inventory_item(id):
    inventory_item = Inventory.query.get(id)
    inventory_item.toggle_status()
    db.session.commit()
    return redirect(url_for('main.inventory'))

#
# @bp.route('/recipe/toggle/<rec>/<id>', methods=['GET', 'POST'])
# def toggle_recipe_item(id, rec):
#     inventory_item = Inventory.query.get(id)
#     id = Recipe.query.get(rec)
#     inventory_item.toggle_status()
#     db.session.commit()
#     return redirect('/recipe/<rec>')
