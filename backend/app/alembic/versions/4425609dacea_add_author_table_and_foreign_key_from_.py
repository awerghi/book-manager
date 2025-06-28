"""add author table and foreign key from book

Revision ID: 4425609dacea
Revises: 9b7ea101b32f
Create Date: 2025-06-28 11:01:36.907772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4425609dacea'
down_revision: Union[str, Sequence[str], None] = '9b7ea101b32f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "author",
        sa.Column("id",sa.INTEGER(),primary_key=True),
        sa.Column("name",sa.String(),nullable=True),
        sa.Column("number_of_published_books", sa.INTEGER(), nullable=True))

    with op.batch_alter_table("Book", recreate="always") as batch_op:
        batch_op.add_column(sa.Column("author_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "fk_book_author",
            "author",       # target table
            ["author_id"],  # local column
            ["id"],         # target column
            ondelete="SET NULL"  # optional behavior
        )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("author")

