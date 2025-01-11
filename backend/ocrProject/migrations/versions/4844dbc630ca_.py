"""empty message

Revision ID: 4844dbc630ca
Revises: 089a50677eaf
Create Date: 2025-01-08 14:05:12.687601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4844dbc630ca'
down_revision: Union[str, None] = '089a50677eaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('gemini_translation', sa.JSON(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurant', 'gemini_translation')
    # ### end Alembic commands ###
