"""initial

Revision ID: f48a45b243a4
Revises: 
Create Date: 2022-07-30 00:41:28.499383

"""
from alembic import op
from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String
from sqlalchemy_utils.types.uuid import UUIDType


# revision identifiers, used by Alembic.
revision = 'f48a45b243a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "url",
        Column("id", Integer(), primary_key=True),
        Column("short_id", String(length=7), unique=False),
        Column("source_url", String(length=255), nullable=False),
        PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_short_id"), "url", ["short_id"], unique=True
    )
    op.create_index(
        op.f("ix_source_url"), "url", ["source_url"], unique=False
    )


def downgrade():
    op.drop_index(
        op.f("ix_short_id"), table_name="url"
    )
    op.drop_index(
        op.f("ix_source_url"), table_name="url"
    )
    op.drop_table("url")

