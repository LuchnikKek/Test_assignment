from src.utils.repository import AbstractRepository


class BaseService:
    def __init__(self, repository: AbstractRepository):
        self._repository = repository

    async def get_users(self) -> list:
        users = await self._repository.find_all()
        return users
