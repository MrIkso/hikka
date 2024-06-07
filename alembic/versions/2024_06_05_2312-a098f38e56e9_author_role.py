"""Author role

Revision ID: a098f38e56e9
Revises: 94694e39413e
Create Date: 2024-06-05 23:12:30.859114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a098f38e56e9'
down_revision = '94694e39413e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service_content_author_roles',
    sa.Column('name_en', sa.String(), nullable=True),
    sa.Column('name_ua', sa.String(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('slug', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service_content_author_roles_slug'), 'service_content_author_roles', ['slug'], unique=False)
    op.create_table('service_relation_manga_author_roles',
    sa.Column('author_id', sa.Uuid(), nullable=False),
    sa.Column('role_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['service_content_manga_authors.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['service_content_author_roles.id'], ),
    sa.PrimaryKeyConstraint('author_id', 'role_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_relation_manga_author_roles')
    op.drop_index(op.f('ix_service_content_author_roles_slug'), table_name='service_content_author_roles')
    op.drop_table('service_content_author_roles')
    # ### end Alembic commands ###