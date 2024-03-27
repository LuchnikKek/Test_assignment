from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.core.constants import FriendRequestStatus


class FriendsSchemaOrmMixin(BaseModel):
    """Mixin для всех схем с ConfigDict."""

    model_config = ConfigDict(from_attributes=True)


class FriendsSchemaPost(FriendsSchemaOrmMixin):
    """Схема, отправляемая при связывании людей в дружеские отношения."""

    request_user_id: UUID
    accept_user_id: UUID
    status: FriendRequestStatus = FriendRequestStatus.ACCEPTED
