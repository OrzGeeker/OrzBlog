"""empty message

Revision ID: d9ceee810c03
Revises: 4b8644720dc7
Create Date: 2018-06-30 22:57:43.499368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ceee810c03'
down_revision = '4b8644720dc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.drop_column('user', 'abount_me')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('abount_me', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
