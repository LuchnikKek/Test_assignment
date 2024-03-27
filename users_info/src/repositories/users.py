import sqlalchemy as sa

from src.models.users import UsersOrm
from src.utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = UsersOrm

    async def find(self, **filter_by):
        opts = sa.orm.selectinload(self.model.emails)
        return await super().find(options=opts, **filter_by)
