from flask import render_template
from app import app

import json
with open('data/recipes.json') as f:
    recipes_struct = json.load(f)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Super Sario'}
    recipes = [
        {
            "@context": "http://schema.org/",
            "@type": "Recipe",
            "name": "Chana Masala",
            "author": {
              "@type": "Person",
              "name": "Leanne Brown"
            },
            "datePublished": "2015-03-03 17:00:00",
            "image": "https://www.leannebrown.com/wp-content/uploads/2015/03/chana-masala.jpeg",
            "description": "Chickpeas cooked in a spicy, curried tomato sauce.",
            "recipeYield": "2",
            "prepTime": "PTM",
            "cookTime": "PTM",
            "recipeIngredient": [
              "1/2 Tbsp ghee or butter",
              "1 tsp cumin seeds",
              "1/2 cup onion (diced)",
              "1 tsp garlic (finely chopped)",
              "1 tsp ginger root (grated)",
              "1/2  jalapeno (finely diced)",
              "3 tsp coriander powder",
              "1 tsp turmeric",
              "1/4 tsp cayenne (powder)",
              "1/2 tsp garam masala (powder)",
              "1 tsp paprika (smoked)",
              "1/2 tsp salt",
              "1 cup tomatoes (canned (pureed))",
              "2 1/2 cups chickpeas (cooked and drained)",
              "1/2 cup water",
              "cilantro (fresh)",
              "yogurt"
            ],
            "recipeInstructions": [
              "Measure out all the spices except the cumin seeds and put them in a small bowl.",
              "Let the ghee (clarified butter) melt in a small saucepan over medium-low heat. (Ghee is the traditional Indian choice, but you can substitute butter if you can't find ghee.) Once the ghee begins to sizzle, add the cumin seeds and stir for about 5 seconds. Add the onion and saute for 2 minutes. Add the garlic and cook for 1 minute. Add the ginger and jalapeno and cook for 1 more minute. Add the spices and then the pureed tomatoes. Mix, then put a lid on the pan and let everything cook down for 5 to 10 minutes.",
              "Once the tomato has reduced and the ghee starts to separate from the sauce, add the chickpeas and water. Mix, then bring it to a boil before reducing to a simmer. Cook for 10 minutes, then squish a few chickpeas with a spoon to thicken the sauce. Garnish with yogurt and cilantro. For a full meal, serve over rice or with roti."
            ],
            "recipeCategory": "Main course"
        },
        {
            "@context": "http://schema.org/",
            "@type": "Recipe",
            "name": "Chickpea Vegetable Bowl with Peanut Dressing",
            "author": {
              "@type": "Person",
              "name": "Leanne Brown"
            },
            "datePublished": "2017-02-28 11:00:38",
            "image": "https://www.leannebrown.com/wp-content/uploads/2017/02/chickpea-and-veg-bowl.jpg",
            "description": "A versatile, hearty meal-worthy salad based on chickpeas and tossed with a nutty dressing. This wintery version involves cabbage, carrots and scallions!",
            "recipeYield": "4",
            "recipeIngredient": [
              "1/4 cup peanut butter",
              "1 Tbsp sriracha or sambal oelek",
              "2  limes (juiced (about 1/4 cup juice))",
              "1 Tbsp fish sauce ((optional))",
              "salt (to taste)",
              "water (as needed)",
              "2 cups dried chickpeas (or 2 cans chickpeas, drained and rinsed)",
              "1 1/2 tsps salt",
              "1 small red cabbage (shredded)",
              "2 large carrots (shredded or grated)",
              "1/3 bunch scallions (chopped)",
              "cilantro (to taste (optional))",
              "peanuts (chopped (optional))"
            ],
            "recipeInstructions": [
              "Cook the chickpeas (skip this step if using canned chickpeas): Rinse the dried chickpeas and let them sit submerged in cold water for a few minutes. Pick out any chickpeas or random bits that rise to the top and discard. Drain the rinsed chickpeas and place into a pot along with the salt and cover with at least 4 inches of water above the line of chickpeas. Bring to a boil on high heat, then turn the heat to low and maintain a gentle simmer. Check on the beans every half hour or so, making sure to keep them covered with water if it boils away. Cook for 1 1/2 to 3 hours, until the chickpeas are soft and cooked through. To lessen the simmering time, you can soak the chickpeas in water overnight, which can cut down on cooking time by an hour or more. Once chickpeas are cooked, store them in their cooking liquid, but drain them before adding to salad.",
              "In a large bowl whisk together the peanut butter, sriracha or sambal oelek, lime juice, fish sauce (if using), and a sprinkling of salt. If you have it around and think the dressing could use a more salty hit, add a teaspoon or so of soy sauce and taste. At this point, the dressing will still be fairly thick and sticky, so drizzle a bit of water in and whisk. Keep adding water and whisking until you have a pourable dressing. Taste and add more salt, lime juice, or peanut butter to your liking.",
              "In the bowl with the dressing, add the chickpeas, shredded cabbage, and carrots and toss it all together with tongs until everything is coated.",
              "Pile it into bowls and top with scallions, chopped cilantro, and peanuts if desired."
            ],
            "recipeCategory": "Main course"
        },

    ]
    return render_template('index.html', title='Home', user=user, recipes=recipes_struct)
