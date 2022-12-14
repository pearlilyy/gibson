"""create fix

Revision ID: fdcd55c101db
Revises: 224ee4b0a4cd
Create Date: 2022-12-13 16:12:24.601357

"""
from alembic import op
from psycopg2 import Timestamp
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdcd55c101db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('fix',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.Integer(),
                              sa.ForeignKey('users.id'), nullable=False),
                    sa.Column('guitar_info', sa.String(
                        length=50), nullable=False),
                    sa.Column('attached_file', sa.String(
                        length=30), nullable=False),
                    sa.Column('post_date', sa.TIMESTAMP, nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('fix')
