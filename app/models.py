from datetime import datetime
from app import db

recipe_ingredients = db.Table('recipe_ingredients',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(64), index=True, unique=True)
    ingredient_category = db.Column(db.Text)
    ingredient_subcategory = db.Column(db.Text)
    storage_location = db.Column(db.Text)
    is_present = db.Column(db.Boolean)
    include = db.Column(db.Boolean)

    def __repr__(self):
        return '<Ingredient {}>'.format(self.ingredient_name)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(128), index=True, unique=True)
    image = db.Column(db.Text)
    description = db.Column(db.Text)
    recipe_category = db.Column(db.Text)
    source = db.Column(db.Text)
    recipe_yield = db.Column(db.Text)
    include = db.Column(db.Boolean)
    ingredients = db.relationship('Ingredient', secondary=recipe_ingredients, lazy='subquery',
        backref=db.backref('recipes', lazy=True))
    instructions = db.relationship('Instruction', backref='recipe', lazy=True)

    def __repr__(self):
        return '<Recipe {}>'.format(self.recipe_name)

class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instruction_text = db.Column(db.Text)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
