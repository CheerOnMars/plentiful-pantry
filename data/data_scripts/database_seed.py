import os
import json
from app import db, models as m


def get_recipes():
    recipes_file = os.path.join(os.path.dirname(__file__), '..', 'recipes.json')
    # import pdb; pdb.set_trace()
    with open(recipes_file) as f:
        return json.load(f)


def create_or_retrieve_ingredient(record):
    """Create or retrieve an ingredient.

    If the ingredient exists load and return the Model instance.
    Otherwise create the ingredient and return the Model instance.
    """
    ing = m.Ingredient.query.filter_by(ingredient_name=record).first()
    if not ing:
        ing = m.Ingredient(ingredient_name=record)
        db.session.add(ing)
        db.session.commit()

    return ing

for recipe in get_recipes():
    print(f"Creating recipe {recipe['name']}")
    ingredients = []

    for ingredient in recipe['recipeIngredient']:
        ingredients.append(create_or_retrieve_ingredient(ingredient))

    instructions = "\n".join(recipe['recipeInstructions'])

    rec = m.Recipe(
        recipe_name=recipe['name'],
        description=recipe['description'],
        recipe_category=recipe['recipeCategory'],
        image=recipe['image'],
        recipe_yield=recipe['recipeYield'],
        ingredients=ingredients,
        instructions=[m.Instruction(instruction_text=instructions)]
    )
    db.session.add(rec)
    db.session.commit()
