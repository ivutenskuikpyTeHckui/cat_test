"""Корректировка моделей Cat и Breed

Revision ID: 2d1180f6a722
Revises: 05c415b1b4de
Create Date: 2024-10-02 21:13:44.759619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d1180f6a722'
down_revision: Union[str, None] = '05c415b1b4de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
