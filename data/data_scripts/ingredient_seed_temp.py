import os
import json
import csv
from app import db, models as m

""" Seed Ingredient """
def get_ingredients():
    with open('data/ingredients.csv', 'r') as f:
        reader = csv.reader(f)
        recipe_list = list(reader)
        return recipe_list

for ingredient in get_ingredients():
    ing = m.Ingredient(
        name=ingredient[0].capitalize(),
        category=ingredient[1],
        is_present= True if ingredient[2] == "True" else False,
        is_included = True
    )

    db.session.add(ing)
    db.session.commit()

# """ Seed Recipe """
# def get_recipes():
#     recipes_file = os.path.join(os.path.dirname(__file__), '..', 'recipes.json')
#     # import pdb; pdb.set_trace()
#     with open(recipes_file) as f:
#         return json.load(f)
#
# def create_or_retrieve_ingredient(record):
#     """Create or retrieve an ingredient.
#
#     If the ingredient exists load and return the Model instance.
#     Otherwise create the ingredient and return the Model instance.
#     """
#     ing = m.RecipeItem.query.filter_by(ingredient_text=record).first()
#     if not ing:
#         ing = m.RecipeItem(ingredient_text=record)
#         db.session.add(ing)
#         db.session.commit()
#
#     return ing
#
# def create_instruction(record):
#     """Create or retrieve an instruction.
#
#     If the instruction exists load and return the Model instance.
#     Otherwise create the instruction and return the Model instance.
#     """
#     step = m.Instruction.query.filter_by(text=record).first()
#     if not step:
#         step = m.Instruction(text=record)
#         db.session.add(step)
#         db.session.commit()
#
#     return step
#
# def create_or_retrieve_category(record):
#     """Create or retrieve an category.
#
#     If the category exists load and return the Model instance.
#     Otherwise create the ingredicategoryent and return the Model instance.
#     """
#     cat = m.Category.query.filter_by(name=record).first()
#     if not cat:
#         cat = m.Category(name=record)
#         db.session.add(cat)
#         db.session.commit()
#
#     return cat
#
# for recipe in get_recipes():
#     # print(f"Creating recipe {recipe['name']}")
#     ingredients = []
#     categories = []
#     instructions = []
#
#     for ingredient in recipe['recipeIngredient']:
#         ingredients.append(create_or_retrieve_ingredient(ingredient))
#
#     for instruction in recipe['recipeInstructions']:
#         instructions.append(create_instruction(instruction))
#
#     categories.append(create_or_retrieve_category(recipe['recipeCategory']))
#
#     rec = m.Recipe(
#         name=recipe['name'],
#         image=recipe['image'],
#         description=recipe['description'],
#         category=recipe['recipeCategory'],
#         source = "Good and Cheap by Leann Brown",
#         recipe_yield=recipe['recipeYield'],
#         url=recipe['recipeURL'],
#         is_included=True,
#         ingredients=ingredients,
#         instructions=instructions
#     )
#     db.session.add(rec)
#     db.session.commit()
