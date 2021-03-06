"""progress table

Revision ID: 6a1650a56cd4
Revises: d1a60d23498a
Create Date: 2021-04-30 11:44:33.480080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6a1650a56cd4"
down_revision = "d1a60d23498a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "progress",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("high_a", sa.Boolean(), nullable=True),
        sa.Column("high_b", sa.Boolean(), nullable=True),
        sa.Column("high_c", sa.Boolean(), nullable=True),
        sa.Column("high_d", sa.Boolean(), nullable=True),
        sa.Column("low_a", sa.Boolean(), nullable=True),
        sa.Column("low_b", sa.Boolean(), nullable=True),
        sa.Column("low_c", sa.Boolean(), nullable=True),
        sa.Column("low_d", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_progress_user_id"), "progress", ["user_id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_progress_user_id"), table_name="progress")
    op.drop_table("progress")
    # ### end Alembic commands ###
