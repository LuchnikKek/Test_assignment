from src.utils.repository import AbstractRepository


class UsersService:
    def __init__(self, users_repository: AbstractRepository):
        self.users_repository = users_repository

    async def get_users(self) -> list:
        users = await self.users_repository.find_all()
        return users
