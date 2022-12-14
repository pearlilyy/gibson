"""create users

Revision ID: 224ee4b0a4cd
Revises: 
Create Date: 2022-12-13 14:56:31.842342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '224ee4b0a4cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('username', sa.String(
                        length=20), nullable=False),
                    sa.Column('password', sa.String(
                        length=50), nullable=False),
                    sa.Column('first_name', sa.String(
                        length=20), nullable=False),
                    sa.Column('last_name', sa.String(
                        length=20), nullable=False),
                    sa.Column('email', sa.String(length=20), nullable=False),
                    sa.Column('phone', sa.String(length=20), nullable=False),
                    sa.Column('reg_date', sa.TIMESTAMP, nullable=False),
                    sa.Column('guitar_type', sa.String(
                        length=50), nullable=False),
                    sa.Column('city', sa.String(length=20), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('users')
