"""Script to recipe details from Good and Cheap."""
import sys
import requests
from bs4 import BeautifulSoup
import csv
import json

with open('list_of_recipes.csv', 'r') as f:
  reader = csv.reader(f)
  recipe_list = list(reader)

recipe_collection = []
for recipe in recipe_list:
    recipe_url = (str(recipe[0]))
    recipe_page = requests.get(recipe_url)
    recipe_soup = BeautifulSoup(recipe_page.content, 'html.parser')
    data = json.loads(recipe_soup.find('script', type='application/ld+json').text)
    recipe_collection.append(data)

with open('recipes.json', 'w') as outfile:
    json.dump(recipe_collection, outfile, indent=2)
