import os
import json
import csv
from app import db, models as m

# ing = m.Ingredient.query.filter(m.Ingredient.name == 'Asian noodles').first()
# print (ing)

""" Seed Inventory """
def get_inventory():
    with open('data/ingredients.csv', 'r') as f:
        reader = csv.reader(f)
        recipe_list = list(reader)
        return recipe_list

for item in get_inventory():
    option = item[0]
    presence = True if item[2] == "True" else False
    ing = m.Ingredient.query.filter_by(name=option).first()
    inv = m.Inventory(
        ingredient=ing,
        is_present=presence,
    )
    print (inv)
    print (ing)
    print (inv.ingredient_id)
    print (inv.is_present)
    import pdb; pdb.set_trace()
    # db.session.add(inv)
    # db.session.commit()
