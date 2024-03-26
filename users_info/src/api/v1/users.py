from fastapi import APIRouter, Depends

from src.api.v1.dependencies import get_users_service
from src.services.users import UsersService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
async def get_users(users_service: UsersService = Depends(get_users_service)) -> list:
    users = await users_service.get_users()
    return users
