from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_async_session
from src.repositories.emails import EmailsRepository
from src.repositories.users import UsersRepository
from src.services.emails import EmailsService
from src.services.users import UsersService


def get_users_service(session: AsyncSession = Depends(get_async_session)):
    return UsersService(UsersRepository(session))


def get_emails_service(session: AsyncSession = Depends(get_async_session)):
    return EmailsService(EmailsRepository(session))
