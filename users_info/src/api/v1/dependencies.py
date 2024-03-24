from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_async_session
from src.repositories.users import UsersRepository
from src.services.users import UsersService


def get_users_service(session: AsyncSession = Depends(get_async_session)):
    return UsersService(UsersRepository(session))
