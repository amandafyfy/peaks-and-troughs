"""attempt table

Revision ID: 53c2a927ac13
Revises: 6a1650a56cd4
Create Date: 2021-04-30 11:46:44.559707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "53c2a927ac13"
down_revision = "6a1650a56cd4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "attempt",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("category", sa.String(length=64), nullable=True),
        sa.Column("question_1_id", sa.Integer(), nullable=True),
        sa.Column("question_1_result", sa.Boolean(), nullable=True),
        sa.Column("question_2_id", sa.Integer(), nullable=True),
        sa.Column("question_2_result", sa.Boolean(), nullable=True),
        sa.Column("question_3_id", sa.Integer(), nullable=True),
        sa.Column("question_3_result", sa.Boolean(), nullable=True),
        sa.Column("question_4_id", sa.Integer(), nullable=True),
        sa.Column("question_4_result", sa.Boolean(), nullable=True),
        sa.Column("question_5_id", sa.Integer(), nullable=True),
        sa.Column("question_5_result", sa.Boolean(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("score", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_attempt_user_id"), "attempt", ["user_id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_attempt_user_id"), table_name="attempt")
    op.drop_table("attempt")
    # ### end Alembic commands ###