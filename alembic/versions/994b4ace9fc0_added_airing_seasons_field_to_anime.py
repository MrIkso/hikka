"""Added airing_seasons field to anime

Revision ID: 994b4ace9fc0
Revises: a4bd5430b3d2
Create Date: 2024-04-03 21:08:39.126609

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "994b4ace9fc0"
down_revision = "a4bd5430b3d2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "service_content_anime",
        sa.Column(
            "airing_seasons",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default="[]",
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("service_content_anime", "airing_seasons")
    # ### end Alembic commands ###
