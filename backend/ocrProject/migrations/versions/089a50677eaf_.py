"""empty message

Revision ID: 089a50677eaf
Revises: 22fddef7389e
Create Date: 2025-01-06 11:23:39.409338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '089a50677eaf'
down_revision: Union[str, None] = '22fddef7389e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('review_score', sa.Float(), nullable=False),
    sa.Column('open_time', sa.String(), nullable=False),
    sa.Column('phone_num', sa.String(), nullable=False),
    sa.Column('homepage', sa.String(), nullable=False),
    sa.Column('summary_reviews', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('reviews', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('answer')
    op.drop_table('question')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('subject', sa.VARCHAR(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('restaurant')
    # ### end Alembic commands ###
