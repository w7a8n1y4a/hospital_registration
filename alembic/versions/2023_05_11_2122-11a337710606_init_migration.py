"""init migration

Revision ID: 11a337710606
Revises: 
Create Date: 2023-05-11 21:22:08.631230

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '11a337710606'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_type', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('doctor_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('diagnosis_comment', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('date_of_diagnosis', sa.Date(), nullable=False),
    sa.Column('id_diagnosis_status', sa.Integer(), nullable=False),
    sa.Column('disease_code', sqlmodel.sql.sqltypes.AutoString(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('gender', postgresql.ENUM('Жен.', 'Муж.', 'Неопределенный', name='genders'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('second_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('patronymic', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('appointments')
    # ### end Alembic commands ###
