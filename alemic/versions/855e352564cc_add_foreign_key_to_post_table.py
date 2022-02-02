"""add foreign key to post table

Revision ID: 855e352564cc
Revises: 5f68358d29be
Create Date: 2022-02-01 19:59:35.506201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '855e352564cc'
down_revision = '5f68358d29be'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')



    pass
