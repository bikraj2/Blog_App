"""Added User as Foreign Key

Revision ID: 7db7dbb39806
Revises: 2500899b0bdf
Create Date: 2025-03-02 18:44:00.885565

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7db7dbb39806'
down_revision: Union[str, None] = '2500899b0bdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('author_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'blog', 'user', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog', type_='foreignkey')
    op.drop_column('blog', 'author_id')
    # ### end Alembic commands ###
