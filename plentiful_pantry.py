from app import create_app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
    'Recipe': Recipe,
    'Ingredient': Ingredient,
    'Instruction': Instruction,
    'Category': Category,
    'RecipeIngredient': RecipeIngredient,
    'Inventory': Inventory,
    'Substitution': Substitution}
