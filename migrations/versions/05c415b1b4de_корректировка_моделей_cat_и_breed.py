"""Корректировка моделей Cat и Breed

Revision ID: 05c415b1b4de
Revises: f2fb8028f9c3
Create Date: 2024-10-02 21:05:32.155078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05c415b1b4de'
down_revision: Union[str, None] = 'f2fb8028f9c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cat', sa.Column('color', sa.String(), nullable=False, max_length=24))
    op.add_column('cat', sa.Column('age', sa.Integer(), nullable=False))
    op.add_column('cat', sa.Column('description', sa.String(), nullable=False, max_length=256))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cat', 'description')
    op.drop_column('cat', 'age')
    op.drop_column('cat', 'color')
    # ### end Alembic commands ###
