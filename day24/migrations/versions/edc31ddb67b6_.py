"""empty message

Revision ID: edc31ddb67b6
Revises: a1081a5fc849
Create Date: 2020-10-09 15:35:14.837705

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'edc31ddb67b6'
down_revision = 'a1081a5fc849'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('_s_password', sa.String(length=256), nullable=True))
    op.drop_column('student', 's_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('s_password', mysql.VARCHAR(length=256), nullable=True))
    op.drop_column('student', '_s_password')
    # ### end Alembic commands ###
