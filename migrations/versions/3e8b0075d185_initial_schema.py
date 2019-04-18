"""initial schema

Revision ID: 3e8b0075d185
Revises:
Create Date: 2019-03-27 12:29:51.769893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3e8b0075d185"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("products")
