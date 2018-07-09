import json

json_data = open('recipe_collection.json').read()
data = json.loads(json_data)

ingredient_list = []

for recipe in data:
    ingredient_list += (recipe["recipeIngredient"])

print (ingredient_list)
print (len(ingredient_list))

unique_ingredients = ['2 large eggs (lightly beaten)', '1/2 cup milk', '1  egg', 'Salt and pepper']

for ingredient in ingredient_list:
    if ingredient in unique_ingredients:
        print ("It's included!")
    else:
        unique_ingredients.append(ingredient)


# with open('ingredients.txt', 'w') as outfile:
#     json.dump(unique_ingredients, outfile)

print (len(unique_ingredients))

for each in unique_ingredients:
    with open('ingredients.csv','a', newline="\n") as outfile:
        outfile.write(each + ", \n"  )
