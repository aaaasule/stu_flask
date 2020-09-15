"""empty message

Revision ID: b6be5cb94402
Revises: 
Create Date: 2020-09-15 09:34:30.226003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6be5cb94402'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a_name', sa.String(length=16), nullable=True),
    sa.Column('a_breed', sa.String(length=16), nullable=True),
    sa.Column('a_color', sa.String(length=16), nullable=True),
    sa.Column('c_eat', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('a_name')
    )
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a_name', sa.String(length=16), nullable=True),
    sa.Column('a_breed', sa.String(length=16), nullable=True),
    sa.Column('a_color', sa.String(length=16), nullable=True),
    sa.Column('d_legs', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('a_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dogs')
    op.drop_table('cats')
    # ### end Alembic commands ###
