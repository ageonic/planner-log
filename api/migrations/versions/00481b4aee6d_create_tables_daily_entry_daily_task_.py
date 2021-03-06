"""create tables: daily_entry, daily_task_entry

Revision ID: 00481b4aee6d
Revises: e56d8ac700e9
Create Date: 2021-09-07 18:41:22.081045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00481b4aee6d'
down_revision = 'e56d8ac700e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_daily_entry_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_daily_entry'))
    )
    op.create_table('daily_task_entry',
    sa.Column('daily_entry_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('complete', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['daily_entry_id'], ['daily_entry.id'], name=op.f('fk_daily_task_entry_daily_entry_id_daily_entry')),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], name=op.f('fk_daily_task_entry_task_id_task')),
    sa.PrimaryKeyConstraint('daily_entry_id', 'task_id', name=op.f('pk_daily_task_entry'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_task_entry')
    op.drop_table('daily_entry')
    # ### end Alembic commands ###
