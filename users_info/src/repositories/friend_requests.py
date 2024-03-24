from src.models.friendships import FriendRequestsOrm
from src.utils.repository import SQLAlchemyRepository


class FriendsRequestsRepository(SQLAlchemyRepository):
    model = FriendRequestsOrm
