"""NEW COL auto-vote

Revision ID: 8864e7602ec9
Revises: 0bfe4299c9e7
Create Date: 2022-02-01 20:23:08.124902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8864e7602ec9'
down_revision = '0bfe4299c9e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
