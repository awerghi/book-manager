"""add publication date to book info

Revision ID: 9d49824bf5a7
Revises: 
Create Date: 2025-06-27 23:35:32.067274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d49824bf5a7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column('Book',sa.Column('publication_date',sa.String(),nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('Book','publication_date')
