from datetime import datetime
from app import db

recipe_ingredients = db.Table('recipe_ingredients',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    category = db.Column(db.Text)
    subcategory = db.Column(db.Text)
    storage_location = db.Column(db.Text)
    is_present = db.Column(db.Boolean)
    is_included = db.Column(db.Boolean)

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
    is_included = db.Column(db.Boolean)
    # instruction_list = db.Column(db.Text)
    ingredients = db.relationship('Ingredient', secondary=recipe_ingredients, lazy='subquery',
        backref=db.backref('recipes', lazy=True))
    instructions = db.relationship('Instruction', backref='recipe', lazy=True)

    def __repr__(self):
        return '<Recipe {}>'.format(self.name)

class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
