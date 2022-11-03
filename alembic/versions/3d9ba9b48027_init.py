"""init

Revision ID: 3d9ba9b48027
Revises: 
Create Date: 2022-11-03 01:41:11.081766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d9ba9b48027'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id_user',sa.Integer, primary_key=True),
        sa.Column('first_name',sa.String, nullable=False),
        sa.Column('last_name', sa.String),
        sa.Column('seniority_lvl',sa.Integer, nullable=False),
        sa.Column('associated',sa.Boolean, nullable=False),
        sa.Column('badge',sa.String),
        sa.Column('manager_id',sa.Integer, sa.ForeignKey("users.id_user"))
    )

    op.create_table(
        'tribus',
        sa.Column('id_tribus',sa.Integer, primary_key=True),
        sa.Column('name',sa.String, nullable=False)
    )

    op.create_table(
        'associated',
        sa.Column("id_user", sa.Integer, sa.ForeignKey("users.id_user"), primary_key=True),
        sa.Column("id_tribus", sa.Integer, sa.ForeignKey("tribus.id_tribus"), primary_key=True)
    )

    
def downgrade():
    op.drop_table('associated')
    op.drop_table('users')
    op.drop_table('tribus')

