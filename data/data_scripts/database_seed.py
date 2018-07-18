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
    ing = m.Ingredient.query.filter_by(name=record).first()
    if not ing:
        ing = m.Ingredient(name=record)
        db.session.add(ing)
        db.session.commit()

    return ing

def create_or_retrieve_category(record):
    """Create or retrieve an category.

    If the category exists load and return the Model instance.
    Otherwise create the ingredicategoryent and return the Model instance.
    """
    cat = m.Category.query.filter_by(name=record).first()
    if not cat:
        cat = m.Category(name=record)
        db.session.add(cat)
        db.session.commit()

    return cat

for recipe in get_recipes():
    # print(f"Creating recipe {recipe['name']}")
    ingredients = []
    categories = []

    for ingredient in recipe['recipeIngredient']:
        ingredients.append(create_or_retrieve_ingredient(ingredient))

    instructions = "\n".join(recipe['recipeInstructions'])

    categories.append(create_or_retrieve_category(recipe['recipeCategory']))

    rec = m.Recipe(
        name=recipe['name'],
        image=recipe['image'],
        description=recipe['description'],
        category=recipe['recipeCategory'],
        source = "Good and Cheap by Leann Brown",
        recipe_yield=recipe['recipeYield'],
        url=recipe['recipeURL'],
        is_included=True,
        # instruction_list=recipe['recipeInstructions'],
        ingredients=ingredients,
        instructions=[m.Instruction(text=instructions)],
        categories=categories
    )
    db.session.add(rec)
    db.session.commit()
