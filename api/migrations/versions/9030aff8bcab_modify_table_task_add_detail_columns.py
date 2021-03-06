"""modify table: task - add detail columns

Revision ID: 9030aff8bcab
Revises: 3c2f1b6a5e5a
Create Date: 2021-09-05 00:52:48.649910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9030aff8bcab'
down_revision = '3c2f1b6a5e5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('due_date', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_date', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('created_date')
        batch_op.drop_column('due_date')
        batch_op.drop_column('description')

    # ### end Alembic commands ###
