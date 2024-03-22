"""Base models and relations

Revision ID: 01
Revises:
Create Date: 2024-03-23 02:29:46.003475

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "01"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "emails",
        sa.Column("address", sa.String(length=100), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("address"),
    )
    op.create_table(
        "friend_requests",
        sa.Column("request_user_id", sa.Uuid(), nullable=False),
        sa.Column("accept_user_id", sa.Uuid(), nullable=False),
        sa.Column("status", sa.Enum("REQUESTED", "ACCEPTED", "DECLINED", name="friendrequeststatus"), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("firstname", sa.String(length=100), nullable=False),
        sa.Column("lastname", sa.String(length=100), nullable=False),
        sa.Column("patronymic", sa.String(length=100), nullable=True),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.Column("country_code", sa.String(length=2), nullable=True),
        sa.Column("gender", sa.Enum("MALE", "FEMALE", "NOT_APPLICABLE", name="gender"), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.CheckConstraint("age > 0", name="check_users_age_positive"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("lastname", name="unique_users_lastname_ix"),
    )
    op.create_index("users_lastname_ix", "users", ["lastname"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("users_lastname_ix", table_name="users")
    op.drop_table("users")
    op.drop_table("friend_requests")
    op.drop_table("emails")
    op.execute("DROP TYPE IF EXISTS friendrequeststatus")
    op.execute("DROP TYPE IF EXISTS gender")
    # ### end Alembic commands ###
