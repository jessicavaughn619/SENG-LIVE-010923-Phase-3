"""Update pet and owner relationship

Revision ID: 5534adfd0eb2
Revises: 91ac356eee44
Create Date: 2023-04-03 14:21:57.402390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5534adfd0eb2'
down_revision = '91ac356eee44'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'pets', 'owners', ['owner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pets', type_='foreignkey')
    # ### end Alembic commands ###
