from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, email
from src.models.users import UsersOrm
from src.utils.mixins import TimestampedMixin, UuidMixin

if TYPE_CHECKING:
    from .users import UsersOrm


class EmailsOrm(UuidMixin, TimestampedMixin, Base):
    """ORM-модель адреса электронной почты.

    Attributes:
        address: Адрес электронной почты. Валидация с помощью Pydantic.
        user: Содержит ссылку на пользователя, владельца электронной почты.
    """

    __tablename__ = "emails_table"

    address: Mapped[email] = mapped_column(unique=True)

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users_table.id", ondelete="CASCADE"))
    user: Mapped["UsersOrm"] = relationship(back_populates="emails")
