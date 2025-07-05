"""change primary key to isbn

Revision ID: c3e5cb0b375e
Revises: 4425609dacea
Create Date: 2025-07-05 14:34:51.543257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3e5cb0b375e'
down_revision: Union[str, Sequence[str], None] = '4425609dacea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Step 1: Create a new temporary table with the desired structure
    op.create_table(
        'book_temp',
        sa.Column('isbn_10', sa.String, nullable=True),
        sa.Column('isbn_13', sa.String, nullable=False, unique=True),
        sa.Column('title', sa.String, nullable=True),
        sa.Column('subtitle', sa.String, nullable=True),
        sa.Column('language', sa.String, nullable=True),
        sa.Column('edition', sa.String, nullable=True),
        sa.Column('publication_date', sa.String, nullable=True),
        sa.Column('author_id', sa.Integer, nullable=True),
        sa.PrimaryKeyConstraint('isbn_13')
    )

    # Step 2: Copy the data from the old table to the new one
    op.execute('''
        INSERT INTO book_temp (isbn_10, isbn_13, title, subtitle, language, edition, publication_date, author_id)
        SELECT isbn_10, isbn_13, title, subtitle, language, edition, publication_date, author_id
        FROM Book
    ''')

    # Step 3: Drop the old table
    op.drop_table('Book')

    # Step 4: Rename the new table to the original table name
    op.rename_table('book_temp', 'Book')


def downgrade() -> None:
    """Downgrade schema (restore the original structure)."""

    # Step 1: Create the original table back with `id` as primary key
    op.create_table(
        'book_temp',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('isbn_10', sa.String, nullable=True),
        sa.Column('isbn_13', sa.String, nullable=False),
        sa.Column('title', sa.String, nullable=True),
        sa.Column('subtitle', sa.String, nullable=True),
        sa.Column('language', sa.String, nullable=True),
        sa.Column('edition', sa.String, nullable=True),
        sa.Column('publication_date', sa.String, nullable=True),
        sa.Column('author_id', sa.Integer, nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Step 2: Copy the data back into the old structure, keeping `id` as primary key
    op.execute('''
        INSERT INTO book_temp (id, isbn_10, isbn_13, title, subtitle, language, edition, publication_date, author_id)
        SELECT ROWID, isbn_10, isbn_13, title, subtitle, language, edition, publication_date, author_id
        FROM Book
    ''')

    # Step 3: Drop the current table
    op.drop_table('Book')

    # Step 4: Rename the table back to the original one
    op.rename_table('book_temp', 'Book')
