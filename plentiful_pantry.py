from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Recipe': Recipe, 'Ingredient': Ingredient, 'Instruction': Instruction, 'Category': Category, 'RecipeIngredient': RecipeIngredient}
