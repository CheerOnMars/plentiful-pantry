from flask import render_template, flash, redirect, url_for, request, current_app
from app import db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from app.main.forms import EditRecipeForm, EditInventoryForm
from app.main import bp


# import pdb; pdb.set_trace()

@bp.route('/')
@bp.route('/home')
def home():
    user = {'username': 'Super Sario'}
    return render_template('home.html', title='Home')

@bp.route('/recipes/<category>')
def recipes_category(category):
    user = {'username': 'Super Sario'}
    rec_cat_dict = { 'mains': 'Main course', 'sides': 'Side dish', 'salads': 'Salad', 'soups': 'Soup', 'appetizers': 'Appetizer', 'sandwiches': 'Sandwich', 'breads': 'Bread / pastry', 'snacks': 'Snack', 'desserts': 'Dessert', 'drinks': 'Drink', 'condiments': 'Condiment', 'all': 'all'}
    flip_rec_dict = { "Main course": "mains", "Side dish": "sides", "Salad": "salads", "Soup": "soups", "Appetizer": "appetizers", "Sandwich": "sandwiches", "Bread / pastry": "breads", "Snack": "snacks", "Dessert": "desserts", "Drink": "drinks", "Condiment": "condiments", 'all': 'all'}
    categories = Category.query.order_by(Category.name.asc())
    if category == 'all':
        recipes = Recipe.query.order_by(Recipe.name.asc())
    else:
        recipes = Recipe.query.filter_by(category=rec_cat_dict[category])
    return render_template('recipes_category.html', title='Recipes', categories=categories, user=user, recipes=recipes, category=category, rec_cat_dict=rec_cat_dict, flip_rec_dict=flip_rec_dict)


@bp.route('/recipe/<id>')
def recipe(id):
    user = {'username': 'Super Sario'}
    flip_rec_dict = {'Produce': 'produce', 'Dairy/Dairy Substitutes': 'dairy', 'Eggs': 'eggs', 'Meat/Fish': 'meat', 'Condiments': 'condiments', 'Spices': 'spices', 'Nuts': 'nuts', 'Beverage': 'beverages', 'Oils/Vinegars': 'oils', 'Grains': 'grains', 'Beans': 'beans', 'Baking': 'baking', 'Dessert': 'dessert', 'Misc': 'misc', 'All': 'all'}
    ing_cat_dict = {'produce': 'Produce', 'dairy': 'Dairy/Dairy Substitutes', 'eggs': 'Eggs', 'meat': 'Meat/Fish', 'condiments': 'Condiments', 'spices': 'Spices', 'nuts': 'Nuts', 'beverages': 'Beverage', 'oils': 'Oils/Vinegars', 'grains': 'Grains', 'beans': 'Beans', 'baking': 'Baking', 'dessert': 'Dessert', 'misc': 'Misc', 'all': 'All'}
    recipe = Recipe.query.get(id)
    recipe_ingredients = recipe.ingredients
    inventory = Inventory.query.all()
    return render_template('recipe.html', title='Recipe', user=user, recipe=recipe, recipe_ingredients=recipe_ingredients, inventory=inventory, flip_rec_dict=flip_rec_dict, ing_cat_dict=ing_cat_dict)


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


@bp.route('/inventory/<category>')
def inventory(category):
    user = {'username': 'Super Sario'}
    ingredients = Ingredient.query.all()
    flip_rec_dict = {'Produce': 'produce', 'Dairy/Dairy Substitutes': 'dairy', 'Eggs': 'eggs', 'Meat/Fish': 'meat', 'Condiments': 'condiments', 'Spices': 'spices', 'Nuts': 'nuts', 'Beverage': 'beverages', 'Oils/Vinegars': 'oils', 'Grains': 'grains', 'Beans': 'beans', 'Baking': 'baking', 'Dessert': 'dessert', 'Misc': 'misc', 'All': 'all'}
    ing_cat_dict = {'produce': 'Produce', 'dairy': 'Dairy/Dairy Substitutes', 'eggs': 'Eggs', 'meat': 'Meat/Fish', 'condiments': 'Condiments', 'spices': 'Spices', 'nuts': 'Nuts', 'beverages': 'Beverage', 'oils': 'Oils/Vinegars', 'grains': 'Grains', 'beans': 'Beans', 'baking': 'Baking', 'dessert': 'Dessert', 'misc': 'Misc', 'all': 'All'}
    if category == 'all':
        inventory = Inventory.query.all()
    else:
        inventory = Inventory.query.join(Inventory, Ingredient.inventory).filter(Ingredient.category == ing_cat_dict[category])
    return render_template('inventory.html', title='Inventory', user=user, inventory=inventory, ing_cat_dict=ing_cat_dict, category=category, flip_rec_dict=flip_rec_dict)


@bp.route('/options_category/<category>')
def options_category(category):
    user = {'username': 'Super Sario'}
    rec_cat_dict = { 'mains': 'Main course', 'sides': 'Side dish', 'salads': 'Salad', 'soups': 'Soup', 'appetizers': 'Appetizer', 'sandwiches': 'Sandwich', 'breads': 'Bread / pastry', 'snacks': 'Snack', 'desserts': 'Dessert', 'drinks': 'Drink', 'condiments': 'Condiment'}
    flip_rec_dict = { "Main course": "mains", "Side dish": "sides", "Salad": "salads", "Soup": "soups", "Appetizer": "appetizers", "Sandwich": "sandwiches", "Bread / pastry": "breads", "Snack": "snacks", "Dessert": "desserts", "Drink": "drinks", "Condiment": "condiments"}
    categories = Category.query.order_by(Category.name.asc())
    if category == 'all':
        all_recipes = Recipe.query.order_by(Recipe.name.asc())
        recipes = Recipe.find_options(all_recipes)
    else:
        cat_recipes = Recipe.query.filter_by(category=rec_cat_dict[category])
        recipes = Recipe.find_options(cat_recipes)
    return render_template('options_category.html', title='My Recipes', rec_category=category, categories=categories, user=user, recipes=recipes, rec_cat_dict=rec_cat_dict, flip_rec_dict=flip_rec_dict)

@bp.route('/inventory/toggle/<id>/<category>', methods=['GET', 'POST'])
def toggle_inventory_item(id, category):
    inventory_item = Inventory.query.get(id)
    inventory_item.toggle_status()
    db.session.commit()
    return redirect(url_for('main.inventory', category=category))

@bp.route('/recipe_inventory/toggle/<ingredient>/<category>/<recipe>', methods=['GET', 'POST'])
def toggle_recipe_inventory_item(ingredient, category, recipe):
    inventory_item = Inventory.query.get(ingredient)
    inventory_item.toggle_status()
    db.session.commit()
    return redirect(url_for('main.recipe', id=recipe))
