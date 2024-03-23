from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, email
from src.models.mixins import UuidMixin, TimestampedMixin
from src.models.users import UsersOrm


class EmailsOrm(UuidMixin, TimestampedMixin, Base):
    """ORM-модель адреса электронной почты.

    Attributes:
        address: Адрес электронной почты. Валидация с помощью Pydantic.
        user: Содержит ссылку на пользователя, владельца электронной почты.
    """

    __tablename__ = "emails"

    address: Mapped[email | None] = mapped_column(unique=True)
    user: Mapped["UsersOrm"] = relationship(back_populates="emails")
