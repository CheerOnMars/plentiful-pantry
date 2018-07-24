import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from app.forms import InventoryForm, EditRecipeForm

recipe_options = []
recipe_non_options = []
inventory = Inventory.query.all()
recipes = Recipe.query.all()

# beet_salad = Recipe.query.get(11)

# print (beet_salad)
# cookable = True
# for ingredient in beet_salad.ingredients:
#     print (ingredient.ingredient_id, ingredient.ingredient.name, inventory[ingredient.ingredient_id-1], inventory[ingredient.ingredient_id+1].is_present)
#     # print (inventory[ingredient.ingredient_id].is_present)

    # print (ingredient.ingredient.name)
    # if inventory[ingredient.ingredient_id].is_present == False:
    #     cookable = False
    #     print (cookable)
    #     print ()

# inventory = Inventory.query.all()
#
# print (cookable)
#
# if cookable == True
#
# recipe_options.append(beet_salad)

#
# for ing in inventory:
#     print (ing.is_present)

for recipe in recipes:
    cookable = True
    print (recipe)
    for ingredient in recipe.ingredients:
        if ingredient.ingredient.name != 'water':
            # print (ingredient.ingredient.name, ingredient.ingredient_id )

            # print (ingredient.ingredient.name, ingredient.ingredient_id , inventory[ingredient.ingredient_id-1])
            if inventory[ingredient.ingredient_id-1].is_present == False:
                cookable = False

    if cookable == True:
        recipe_options.append(recipe)

    if cookable == False:
        recipe_non_options.append(recipe)
#
#
print (recipe_options)
print (len(recipe_options))

print (recipe_non_options)
print (len(recipe_non_options))
