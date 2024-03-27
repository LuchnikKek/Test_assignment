from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship

from src.core.constants import Gender
from src.core.db import Base, country_alpha_2, str_100
from src.utils.mixins import TimestampedMixin, UuidMixin

if TYPE_CHECKING:
    from .emails import EmailsOrm


class UsersOrm(UuidMixin, TimestampedMixin, Base):
    """ORM-модель Пользователя.

    Attributes:
        firstname: Имя
        lastname: Фамилия
        patronymic: Отчество
        age: Возраст
        country_code: Код страны
        gender: Пол

        emails: Список вложенных моделей адресов электронной почты.
        friends: Список вложенных моделей друзей.
    """

    __tablename__ = "users_table"
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
    gender: Mapped[Gender]

    emails: Mapped[list["EmailsOrm"]] = relationship(back_populates="user")

    friend_requests: Mapped[list["UsersOrm"]] = relationship(
        "UsersOrm",
        secondary="friend_relationships_table",
        primaryjoin="UsersOrm.id == FriendRelationshipsTable.accept_user_id",
        secondaryjoin="UsersOrm.id == FriendRelationshipsTable.request_user_id",
        back_populates="friend_accepts",
    )

    friend_accepts: Mapped[list["UsersOrm"]] = relationship(
        "UsersOrm",
        secondary="friend_relationships_table",
        primaryjoin="UsersOrm.id == FriendRelationshipsTable.request_user_id",
        secondaryjoin="UsersOrm.id == FriendRelationshipsTable.accept_user_id",
        back_populates="friend_requests",
    )
