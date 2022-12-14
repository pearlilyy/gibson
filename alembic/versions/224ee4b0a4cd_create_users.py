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
    op.execute(
        """
        CREATE TABLE users(
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            reg_date TIMESTAMP NOT NULL,
            guitar_type TEXT,
            city TEXT
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE users;
        """
    )
