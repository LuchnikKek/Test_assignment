# from uuid import UUID
#
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import Mapped, relationship, mapped_column
#
# from src.core.db import Base
# from src.models.enums import FriendRequestStatus
# from src.models.mixins import UuidMixin, CreatedMixin
# from src.models.users import UsersOrm
#
#
# class FriendRequestsOrm(UuidMixin, CreatedMixin, Base):
#     """ORM-модель запроса дружбы.
#
#     Attributes:
#         request_user_id: ID пользователя, отправившего запрос.
#         accept_user_id: ID пользователя, которому адресован запрос.
#         status: Статус запроса. Принимает одно из значений из перечисления FriendRequestStatus.
#     """
#
#     __tablename__ = "friend_requests_table"
#
#     request_user_id: Mapped[UUID]
#     accept_user_id: Mapped[UUID]
#     status: Mapped[FriendRequestStatus]
#
#     user: Mapped["UsersOrm"] = relationship(back_populates="friends")
#     user_id = mapped_column(ForeignKey("users_table.id"))
