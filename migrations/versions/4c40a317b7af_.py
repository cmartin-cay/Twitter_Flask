"""empty message

Revision ID: 4c40a317b7af
Revises: c968c6cabada
Create Date: 2017-02-19 12:02:01.900567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c40a317b7af'
down_revision = 'c968c6cabada'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweet', sa.Column('tweetid', sa.String(length=30), nullable=True))
    op.create_index(op.f('ix_tweet_tweetid'), 'tweet', ['tweetid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tweet_tweetid'), table_name='tweet')
    op.drop_column('tweet', 'tweetid')
    # ### end Alembic commands ###
