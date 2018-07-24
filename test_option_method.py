import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from app.forms import InventoryForm, EditRecipeForm

recipe_options = []

beet_salad = Recipe.query.get(11)

print (beet_salad)

for ingredient in beet_salad.ingredients:
    print (ingredient)

inventory = Inventory.query.all()


for ing in inventory:
    print (ing.is_present)
