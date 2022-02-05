"""add last columns to post table

Revision ID: fc8c4aa208bf
Revises: 855e352564cc
Create Date: 2022-02-01 20:07:14.595580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc8c4aa208bf'
down_revision = '855e352564cc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))


    

    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')


    pass
