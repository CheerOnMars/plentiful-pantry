"""tables

Revision ID: ed7a34042878
Revises: 
Create Date: 2018-07-13 07:58:10.431055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed7a34042878'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ingredient_name', sa.String(length=64), nullable=True),
    sa.Column('ingredient_category', sa.Text(), nullable=True),
    sa.Column('ingredient_subcategory', sa.Text(), nullable=True),
    sa.Column('storage_location', sa.Text(), nullable=True),
    sa.Column('is_present', sa.Boolean(), nullable=True),
    sa.Column('include', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ingredient_ingredient_name'), 'ingredient', ['ingredient_name'], unique=True)
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipe_name', sa.String(length=128), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('recipe_category', sa.Text(), nullable=True),
    sa.Column('source', sa.Text(), nullable=True),
    sa.Column('recipe_yield', sa.Text(), nullable=True),
    sa.Column('include', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recipe_recipe_name'), 'recipe', ['recipe_name'], unique=True)
    op.create_table('instruction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instruction_text', sa.Text(), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_ingredients',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('recipe_id', 'ingredient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_ingredients')
    op.drop_table('instruction')
    op.drop_index(op.f('ix_recipe_recipe_name'), table_name='recipe')
    op.drop_table('recipe')
    op.drop_index(op.f('ix_ingredient_ingredient_name'), table_name='ingredient')
    op.drop_table('ingredient')
    # ### end Alembic commands ###