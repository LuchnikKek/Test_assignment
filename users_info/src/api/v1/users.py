from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.v1.dependencies import get_users_service
from src.schemas.users import (
    UserSchemaFull,
    UserSchemaFullPost,
    UserSchemaShort,
    UserSchemaUUIDMixin,
    str_100_meta,
)
from src.services.users import UsersService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserSchemaShort])
async def get_users(users_service: UsersService = Depends(get_users_service)):
    """Возвращает список всех пользователей"""
    users = await users_service.get_all()
    return users


@router.get("/{lastname}", response_model=UserSchemaFull)
async def get_user(
    lastname: Annotated[str, str_100_meta],
    users_service: UsersService = Depends(get_users_service),
):
    """Возвращает пользователя по фамилии."""
    user = await users_service.get(lastname=lastname)
    return user


@router.post("", response_model=UserSchemaUUIDMixin)
async def post_user(
    user: UserSchemaFullPost,
    users_service: UsersService = Depends(get_users_service),
):
    """Создаёт нового пользователя."""
    user = await users_service.set(data=user)
    return user
