from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class InventoryForm(FlaskForm):
    is_present = BooleanField('Present?', validators=[DataRequired()])
    submit = SubmitField('Save inventory')

class RecipeForm(FlaskForm):
    submit = SubmitField('Save recipe')
