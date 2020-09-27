"""empty message

Revision ID: cb568ce55416
Revises: 2d43a78ca046
Create Date: 2020-09-27 11:04:32.180236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb568ce55416'
down_revision = '2d43a78ca046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('s_name', sa.String(length=16), nullable=True),
    sa.Column('s_age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('school',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('position', sa.String(length=64), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('school')
    op.drop_table('students')
    # ### end Alembic commands ###
