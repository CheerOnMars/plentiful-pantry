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

    def __repr__(self):
        return '<Recipe {}>'.format(self.name)

class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    def __repr__(self):
        return '<Instruction {}>'.format(self.text)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    is_present = db.Column(db.Boolean)

    # ingredient = db.relationship('Ingredient', back_populates='inventory', uselist=True)

    def __repr__(self):
        return '<Inventory {}>'.format(self.is_present)

class Substitution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.Text)
    recipe_ingredient_id = db.Column(db.Integer, db.ForeignKey('recipe_ingredient.id'))

    def __repr__(self):
        return '<Substitution {}>'.format(self.option)
