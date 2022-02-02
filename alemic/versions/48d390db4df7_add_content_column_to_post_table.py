"""add content column to post table

Revision ID: 48d390db4df7
Revises: a5713f994988
Create Date: 2022-02-01 19:38:19.466852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48d390db4df7'
down_revision = 'a5713f994988'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')

    pass
