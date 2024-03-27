import sqlalchemy as sa

from src.core.constants import FriendRequestStatus
from src.core.db import Base

from .users import UsersOrm


class FriendRelationshipsTable(Base):
    __tablename__ = "friend_relationships_table"

    request_user_id: sa.orm.Mapped[list["UsersOrm"]] = sa.orm.mapped_column(
        sa.ForeignKey("users_table.id", ondelete="CASCADE"), primary_key=True
    )
    accept_user_id: sa.orm.Mapped[list["UsersOrm"]] = sa.orm.mapped_column(
        sa.ForeignKey("users_table.id", ondelete="CASCADE"), primary_key=True
    )
    status: sa.orm.Mapped[FriendRequestStatus]
    accept_user: sa.orm.Mapped["UsersOrm"] = sa.orm.relationship("UsersOrm", back_populates="friend_requests")
    request_user: sa.orm.Mapped["UsersOrm"] = sa.orm.relationship("UsersOrm", back_populates="friend_accepts")
