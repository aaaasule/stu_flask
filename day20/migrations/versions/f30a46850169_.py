"""empty message

Revision ID: f30a46850169
Revises: 
Create Date: 2020-09-24 16:39:26.314944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f30a46850169'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('u_name', sa.String(length=16), nullable=True),
    sa.Column('u_age', sa.Integer(), nullable=True),
    sa.Column('a_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['a_id'], ['address.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('u_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('address')
    # ### end Alembic commands ###