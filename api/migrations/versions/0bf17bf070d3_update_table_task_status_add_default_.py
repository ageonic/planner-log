"""update table: task_status - add default column

Revision ID: 0bf17bf070d3
Revises: 6b03990a6cf0
Create Date: 2021-09-13 23:20:49.817909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bf17bf070d3'
down_revision = '6b03990a6cf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_status', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_status', schema=None) as batch_op:
        batch_op.drop_column('default')

    # ### end Alembic commands ###
