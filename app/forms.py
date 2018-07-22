from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, DataRequired, EqualTo
from app.models import Inventory, Ingredient, Recipe, Instruction, RecipeIngredient

class InventoryForm(FlaskForm):
    is_present = BooleanField('Present?', validators=[DataRequired()])
    submit = SubmitField('Save inventory')
    id = IntegerField('Id')
    status = BooleanField('Status?', validators=[DataRequired()])

    def update_inventory(self, id):
        return self

class EditRecipeForm(FlaskForm):
    name = StringField('Recipe Name:', validators=[DataRequired()])
    description = TextAreaField('Description: ')
    recipe_yield = StringField('Yield: ')
    category = StringField('Category: ')
    image_url = StringField('Image URL: ')
    source = StringField('Recipe Creator: ')
    recipe_url = StringField('Recipe URL: ')
    submit = SubmitField('Save recipe')
