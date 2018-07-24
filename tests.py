from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import Recipe, Ingredient, Instruction, Category, RecipeIngredient, Inventory, Substitution
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


if __name__ == '__main__':
    unittest.main(verbosity=2)
