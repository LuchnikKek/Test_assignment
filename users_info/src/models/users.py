from uuid import UUID
from enum import StrEnum, auto

from sqlalchemy import UniqueConstraint, CheckConstraint, Index
from sqlalchemy.orm import relationship, Mapped, mapped_column

from users_info.src.core.db import Base, str_100, country_alpha_2, email
from users_info.src.models.mixins import UuidMixin, TimestampedMixin, CreatedMixin
from users_info.src.utils.inspect import inspect_model


class Gender(StrEnum):
    """
    Перечисление всех полов.
    В соответствии с ISO 5218: https://en.wikipedia.org/wiki/ISO/IEC_5218
    """

    MALE = auto()
    FEMALE = auto()
    NOT_APPLICABLE = auto()


class FriendRequestStatus(StrEnum):
    """Перечисление всех состояний запроса дружбы."""

    REQUESTED = auto()
    ACCEPTED = auto()
    DECLINED = auto()


class UsersOrm(UuidMixin, TimestampedMixin, Base):
    __tablename__ = "users"
    __table_args__ = (
        Index("users_lastname_ix", "lastname"),
        CheckConstraint("age > 0", name="check_users_age_positive"),
        UniqueConstraint("lastname", name="unique_users_lastname_ix"),
    )

    firstname: Mapped[str_100]
    lastname: Mapped[str_100]
    patronymic: Mapped[str_100 | None]
    age: Mapped[int | None]
    country_code: Mapped[country_alpha_2 | None]
    gender: Mapped[Gender | None]

    emails: Mapped[list["EmailsOrm"]] = relationship(back_populates="user")

    friends_list: Mapped[list["FriendRequestsOrm"]] = relationship(
        back_populates="user",
        lazy=True,
        primaryjoin="and_(or_(UsersOrm.id == FriendRequestsOrm.request_user_id, UsersOrm.id == FriendRequestsOrm.accept_user_id), FriendRequestsOrm.status == 'accepted')",  # todo:
    )


class EmailsOrm(UuidMixin, TimestampedMixin, Base):
    __tablename__ = "emails"

    address: Mapped[email | None] = mapped_column(unique=True)
    user: Mapped["UsersOrm"] = relationship(back_populates="emails")


class FriendRequestsOrm(UuidMixin, CreatedMixin, Base):
    __tablename__ = "friend_requests"

    request_user_id: Mapped[UUID]
    accept_user_id: Mapped[UUID]
    status: Mapped[FriendRequestStatus]

    user: Mapped["UsersOrm"] = relationship(back_populates="friend_requests")
