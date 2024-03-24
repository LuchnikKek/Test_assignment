from src.models.users import UsersOrm
from src.utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = UsersOrm
