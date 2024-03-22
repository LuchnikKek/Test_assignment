from enum import StrEnum, auto
from uuid import UUID

from sqlalchemy.orm import Mapped, relationship

from users_info.src.core.db import Base
from users_info.src.models.mixins import UuidMixin, CreatedMixin
from users_info.src.models.users import UsersOrm


class FriendRequestStatus(StrEnum):
    """Перечисление всех состояний запроса дружбы."""

    REQUESTED = auto()
    ACCEPTED = auto()
    DECLINED = auto()


class FriendRequestsOrm(UuidMixin, CreatedMixin, Base):
    __tablename__ = "friend_requests"

    request_user_id: Mapped[UUID]
    accept_user_id: Mapped[UUID]
    status: Mapped[FriendRequestStatus]

    user: Mapped["UsersOrm"] = relationship(back_populates="friend_requests")
