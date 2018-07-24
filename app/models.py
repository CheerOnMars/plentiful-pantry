from datetime import datetime
from app import db

class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))

    recipe = db.relationship('Recipe', back_populates="ingredients")
    ingredient = db.relationship('Ingredient', back_populates="recipes")

    is_optional = db.Column(db.Boolean)
    ingredient_text = db.Column(db.Text)
    substitutions = db.relationship('Substitution', backref='recipeItem', lazy=True)

    def __repr__(self):
        return '<Recipe Item: Recipe({}), Ingredient({}), Optional({})>'.format(
            self.recipe.name,
            self.ingredient.name,
            self.is_optional
        )

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    category = db.Column(db.Text)
    recipes = db.relationship('RecipeIngredient', back_populates='ingredient', uselist=True)
    inventory =  db.relationship('Inventory', backref='ingredient', lazy='dynamic')

    def __repr__(self):
        return '<Ingredient {}>'.format(self.name)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    image = db.Column(db.Text)
    description = db.Column(db.Text)
    category = db.Column(db.Text)
    source = db.Column(db.Text)
    recipe_yield = db.Column(db.Text)
    url = db.Column(db.Text)
    ingredients = db.relationship('RecipeIngredient', back_populates='recipe', uselist=True)
    instructions = db.relationship('Instruction', backref='recipe', lazy=True)
    
    def find_options(set):
        recipe_options = []
        inventory = Inventory.query.all()
        recipes = Recipe.query.all()
        for recipe in recipes:
            cookable = True
            print (recipe)
            for ingredient in recipe.ingredients:
                if ingredient.ingredient.name != 'water':
                    if inventory[ingredient.ingredient_id-1].is_present == False:
                        cookable = False
            if cookable == True:
                recipe_options.append(recipe)
        return recipe_options

    def __repr__(self):
        return '<Recipe {}>'.format(self.name)

class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    is_present = db.Column(db.Boolean)

    # ingredient = db.relationship('Ingredient', back_populates="inventory")
    # ingredient = db.relationship('Ingredient', back_populates='inventory', uselist=True)
    # category = db.Column(db.Text, db.ForeignKey('ingredient.category'))
    # def check_category(self):
    #     return self.ingredient.category

class Substitution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.Text)
    recipe_ingredient_id = db.Column(db.Integer, db.ForeignKey('recipe_ingredient.id'))
