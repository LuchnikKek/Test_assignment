from fastapi import APIRouter, Depends

from src.api.v1.dependencies import get_friends_service
from src.schemas.friends import FriendsSchemaPost
from src.services.friends import FriendsService

router = APIRouter(prefix="/friends", tags=["Friends"])


@router.post("")
async def post_friends(
    friends: FriendsSchemaPost = Depends(),
    friends_service: FriendsService = Depends(get_friends_service),
):
    """Создаёт дружбу между пользователями."""
    return await friends_service.set(friends)
