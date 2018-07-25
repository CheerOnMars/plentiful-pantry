from datetime import datetime, timedelta
import unittest

from app import app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution


if __name__ == '__main__':
    unittest.main(verbosity=2)
