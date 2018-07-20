import os
import json
import csv
from app import db, models as m

""" Seed Recipe and corresponding tables"""
def get_recipes():
    recipes_file = os.path.join(os.path.dirname(__file__), '..', 'recipes.json')
    # import pdb; pdb.set_trace()
    with open(recipes_file) as f:
        return json.load(f)

def create_or_retrieve_recipe_ingredient(record):
    """Create or retrieve an ingredient.

    If the ingredient exists load and return the Model instance.
    Otherwise create the ingredient and return the Model instance.
    """
    # ing = m.Item.query.filter_by(ingredient_text=record).first()
    # if not ing:
    #     ing = m.Item(ingredient_text=record)
    #     db.session.add(ing)
    #     db.session.commit()
    #
    # return ing

for recipe in get_recipes():
    # recipe_ingredients = []
    #
    # for ingredient in recipe['recipeIngredient']:
    #     recipe_ingredients.append(create_or_retrieve_recipe_ingredient(ingredient))

    rec = m.Recipe(
        name=recipe['name'],
        image=recipe['image'],
        description=recipe['description'],
        category=recipe['recipeCategory'],
        source = "Good and Cheap by Leann Brown",
        recipe_yield=recipe['recipeYield'],
        url=recipe['recipeURL'],
        is_included=True,
        # ingredients=recipe_ingredients
    )
    db.session.add(rec)
    db.session.commit()
