from pydantic import BaseModel

from src.utils.repository import SQLAlchemyRepository


class BaseService:
    def __init__(self, repository: SQLAlchemyRepository):
        self._repository = repository

    async def get(self, **filter_by):
        user = await self._repository.find(**filter_by)
        return user

    async def get_all(self, **filter_by) -> list:
        users = await self._repository.find_all(**filter_by)
        return users

    async def set(self, data: BaseModel) -> dict:
        id = await self._repository.add_one(data)
        return {"id": id}
