"""Add employee_id to Onboarding model

Revision ID: 030b7253eef8
Revises: dfca29d95177
Create Date: 2025-03-26 09:52:14.394768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '030b7253eef8'
down_revision = 'dfca29d95177'
branch_labels = None
depends_on = None


def upgrade():
    # Create a new table with the desired structure
    op.create_table('new_onboardings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('orientation', sa.DateTime(), nullable=True),
        sa.Column('forms_complete', sa.Boolean(), nullable=True),
        sa.Column('employee_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_new_onboardings_employee_id_employees')),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data from the old table to the new table
    op.execute('INSERT INTO new_onboardings (id, orientation, forms_complete) SELECT id, orientation, forms_complete FROM onboardings')

    # Drop the old table
    op.drop_table('onboardings')

    # Rename the new table to the old table name
    op.rename_table('new_onboardings', 'onboardings')


def downgrade():
    # Drop the foreign key constraint
    op.drop_constraint(op.f('fk_new_onboardings_employee_id_employees'), 'onboardings', type_='foreignkey')

    # Drop the new column
    op.drop_column('onboardings', 'employee_id')

    # Recreate the old table structure if necessary
    op.create_table('old_onboardings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('orientation', sa.DateTime(), nullable=True),
        sa.Column('forms_complete', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data back from the current table to the old table
    op.execute('INSERT INTO old_onboardings (id, orientation, forms_complete) SELECT id, orientation, forms_complete FROM onboardings')

    # Drop the current table
    op.drop_table('onboardings')

    # Rename the old table back to the original name
    op.rename_table('old_onboardings', 'onboardings')
