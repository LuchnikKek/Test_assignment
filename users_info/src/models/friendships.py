import sqlalchemy as sa

from src.core.db import Base


class FriendRelationshipsTable(Base):
    __tablename__ = "friend_relationships_table"

    request_user_id: sa.orm.Mapped[sa.Uuid] = sa.orm.mapped_column(
        sa.ForeignKey("users_table.id", ondelete="CASCADE"), primary_key=True
    )
    accept_user_id: sa.orm.Mapped[sa.Uuid] = sa.orm.mapped_column(
        sa.ForeignKey("users_table.id", ondelete="CASCADE"), primary_key=True
    )
