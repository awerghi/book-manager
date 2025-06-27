"""remove author from book

Revision ID: 9b7ea101b32f
Revises: 9d49824bf5a7
Create Date: 2025-06-28 00:24:03.842849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b7ea101b32f'
down_revision: Union[str, Sequence[str], None] = '9d49824bf5a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table('Book') as batch_op:
        batch_op.drop_column('author')


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column("Book",sa.Column("author",sa.String(),nullable=True))

