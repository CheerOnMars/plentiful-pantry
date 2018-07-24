import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from app.forms import InventoryForm, EditRecipeForm

recipe_options = []
inventory = Inventory.query.all()

beet_salad = Recipe.query.get(11)

print (beet_salad)
cookable = True
for ingredient in beet_salad.ingredients:
    print (ingredient.ingredient_id, ingredient.ingredient.name, inventory[ingredient.ingredient_id].is_present)
    # print (inventory[ingredient.ingredient_id].is_present)

    # print (ingredient.ingredient.name)
    if inventory[ingredient.ingredient_id].is_present == False:
        cookable = False
        print (cookable)
        print ()

# inventory = Inventory.query.all()
#
print (cookable)

if cookable == True

#
# for ing in inventory:
#     print (ing.is_present)
