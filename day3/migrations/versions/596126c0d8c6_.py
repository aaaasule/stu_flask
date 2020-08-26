"""empty message

Revision ID: 596126c0d8c6
Revises: 
Create Date: 2020-08-26 09:31:37.972072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '596126c0d8c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('s_name', sa.String(length=16), nullable=True),
    sa.Column('s_num', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('student')
    # ### end Alembic commands ###