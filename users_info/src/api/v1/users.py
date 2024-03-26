from fastapi import APIRouter, Depends

from src.api.v1.dependencies import get_users_service
from src.schemas.users import UserSchemaOut, UserSchemaOutShort
from src.services.users import UsersService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserSchemaOutShort])
async def get_users(users_service: UsersService = Depends(get_users_service)):
    users = await users_service.get_all()
    return users


@router.get("/{lastname}", response_model=UserSchemaOut)
async def get_user(
    lastname: str,
    users_service: UsersService = Depends(get_users_service),
):
    user = await users_service.get(lastname=lastname)
    return user
