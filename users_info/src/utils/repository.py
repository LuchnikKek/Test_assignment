from abc import ABC, abstractmethod

import sqlalchemy as sa

from src.core.exceptions import NotFoundError


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict): ...

    @abstractmethod
    async def find_all(self): ...


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: sa.ext.asyncio.AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = sa.insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def find(self, **filter_by):
        stmt = sa.select(self.model).filter_by(**filter_by)

        res = await self.session.execute(stmt)
        try:
            result = res.scalars().one()
        except sa.exc.NoResultFound:
            raise NotFoundError(detail={"msg": "Not found", "params": filter_by})

        return result

    async def find_all(self, **filter_by):
        stmt = sa.select(self.model).filter_by(**filter_by)

        res = await self.session.execute(stmt)
        try:
            result = res.scalars().all()
        except sa.exc.NoResultFound:
            raise NotFoundError(detail={"msg": "Not found", "params": filter_by})

        return result
