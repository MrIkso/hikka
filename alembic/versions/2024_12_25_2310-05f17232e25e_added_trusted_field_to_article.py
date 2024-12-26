"""Added trusted field to article

Revision ID: 05f17232e25e
Revises: 3027a7fff9ca
Create Date: 2024-12-25 23:10:42.752458

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "05f17232e25e"
down_revision = "3027a7fff9ca"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "service_articles",
        sa.Column(
            "trusted", sa.Boolean(), nullable=False, server_default="false"
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("service_articles", "trusted")
    # ### end Alembic commands ###