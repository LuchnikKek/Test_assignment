import sqlalchemy as sa

from src.core.constants import FriendRequestStatus
from src.core.db import Base

FriendRelationships = sa.Table(
    "friend_relationships_table",
    Base.metadata,
    sa.Column("request_user_id", sa.Uuid, sa.ForeignKey("users_table.id", ondelete="CASCADE"), primary_key=True),
    sa.Column("accept_user_id", sa.Uuid, sa.ForeignKey("users_table.id", ondelete="CASCADE"), primary_key=True),
    sa.Column("status", sa.Enum(FriendRequestStatus), nullable=False),
)

# class FriendRequestsOrm(CreatedMixin, Base):
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
#     status: Mapped[FriendRequestStatus]
