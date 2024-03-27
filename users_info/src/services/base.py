from uuid import UUID

from pydantic import BaseModel

from src.utils.repository import SQLAlchemyRepository


class BaseService:
    def __init__(self, repository: SQLAlchemyRepository):
        self._repository = repository

    async def get(self, **filter_by):
        return await self._repository.find(**filter_by)

    async def get_all(self, **filter_by) -> list:
        return await self._repository.find_all(**filter_by)

    async def set(self, data: BaseModel) -> UUID:
        return await self._repository.add_one(data)

    async def put(self, schema: BaseModel, attr: str | None = None):
        return await self._repository.update_if_exists(schema, partial=False, attr=attr)

    async def patch(self, schema: BaseModel, attr: str | None = None):
        return await self._repository.update_if_exists(schema, partial=True, attr=attr)
