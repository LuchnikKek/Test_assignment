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
    return await users_service.get_all()


@router.get("/{lastname}", response_model=UserSchemaFull)
async def get_user(
    lastname: Annotated[str, str_100_meta],
    users_service: UsersService = Depends(get_users_service),
):
    """Возвращает пользователя по фамилии."""
    return await users_service.get(lastname=lastname)


@router.post("", response_model=UserSchemaUUIDMixin)
async def post_user(
    user: UserSchemaFullPost,
    users_service: UsersService = Depends(get_users_service),
):
    """Создаёт нового пользователя."""
    return await users_service.set(user)


@router.put("", response_model=UserSchemaFull)
async def put_user(
    user: UserSchemaFullPost,
    users_service: UsersService = Depends(get_users_service),
):
    """Полностью изменяет пользователя по фамилии."""
    return await users_service.put(user, attr="lastname")


@router.patch("", response_model=UserSchemaFull)
async def patch_user(
    user: UserSchemaFullPost,
    users_service: UsersService = Depends(get_users_service),
):
    """Частично изменяет пользователя по фамилии."""
    return await users_service.patch(user, attr="lastname")
