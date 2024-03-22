from enum import StrEnum, auto

from sqlalchemy import UniqueConstraint, CheckConstraint, Index
from sqlalchemy.orm import relationship, Mapped

from users_info.src.core.db import Base, str_100, country_alpha_2
from users_info.src.models.mixins import UuidMixin, TimestampedMixin


class Gender(StrEnum):
    """
    Перечисление всех полов.
    В соответствии с ISO 5218: https://en.wikipedia.org/wiki/ISO/IEC_5218
    """

    MALE = auto()
    FEMALE = auto()
    NOT_APPLICABLE = auto()


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
