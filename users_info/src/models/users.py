from enum import StrEnum, auto

from sqlalchemy import UniqueConstraint, CheckConstraint, Index
from sqlalchemy.orm import relationship, Mapped

from src.core.db import Base, str_100, country_alpha_2
from src.models.mixins import UuidMixin, TimestampedMixin


class Gender(StrEnum):
    """
    Перечисление всех полов.
    В соответствии с ISO 5218: https://en.wikipedia.org/wiki/ISO/IEC_5218

    Стандарт предусматривает ещё значение 'NOT KNOWN', означающее, что пол не указан.
    Его решил реализовать как NULL в базе, чтобы избежать двойственного значения.
    """

    MALE = auto()
    FEMALE = auto()
    NOT_APPLICABLE = auto()


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
    friends: Mapped[list["FriendRequestsOrm"]] = relationship(
        back_populates="user",
        lazy=True,
        primaryjoin="and_(or_(UsersOrm.id == FriendRequestsOrm.request_user_id, UsersOrm.id == "
        "FriendRequestsOrm.accept_user_id), FriendRequestsOrm.status == 'accepted')",
    )
