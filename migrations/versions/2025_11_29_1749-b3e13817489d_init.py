"""Init

Revision ID: b3e13817489d
Revises: 
Create Date: 2025-11-29 17:49:55.855252
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = 'b3e13817489d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("id_auth", sa.Integer(), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table("user")
