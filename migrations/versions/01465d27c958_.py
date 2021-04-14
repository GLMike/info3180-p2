"""empty message

Revision ID: 01465d27c958
Revises: 7825757bf5e9
Create Date: 2021-04-14 02:10:02.150397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01465d27c958'
down_revision = '7825757bf5e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'favourites', 'cars', ['car_id'], ['id'])
    op.create_foreign_key(None, 'favourites', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favourites', type_='foreignkey')
    op.drop_constraint(None, 'favourites', type_='foreignkey')
    # ### end Alembic commands ###