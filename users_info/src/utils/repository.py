from abc import ABC, abstractmethod
from uuid import UUID

import sqlalchemy as sa
from pydantic import BaseModel

from src.core.exceptions import AlreadyExistsError, NotFoundError


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict): ...

    @abstractmethod
    async def find_all(self): ...


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: sa.ext.asyncio.AsyncSession):
        self.session = session

    async def add_one(self, data: BaseModel) -> UUID:
        """Добавляет одну запись, возвращает её UUID."""
        stmt = sa.insert(self.model).values(**data.dict()).returning(self.model.id)

        try:
            res = await self.session.execute(stmt)
        except sa.exc.IntegrityError:
            raise AlreadyExistsError(detail={"msg": "Record already exists"})

        await self.session.commit()
        return res.scalar_one()

    async def find(self, options=None, **filter_by):
        """Получает запись по запрошенным {key: value}."""

        stmt = sa.select(self.model).filter_by(**filter_by).options(options)

        res = await self.session.execute(stmt)
        try:
            result = res.unique().scalars().one()
        except sa.exc.NoResultFound:
            raise NotFoundError(detail={"msg": "Not found", "params": filter_by})

        return result

    async def find_all(self, **filter_by):
        """Получает все записи по запрошенным {key: value}."""
        stmt = sa.select(self.model).filter_by(**filter_by)

        res = await self.session.execute(stmt)
        try:
            result = res.scalars().all()
        except sa.exc.NoResultFound:
            raise NotFoundError(detail={"msg": "Not found", "params": filter_by})

        return result

    async def update_if_exists(self, schema: BaseModel, partial: bool, attr: str = "id"):
        """
        Изменяет запись в базе.

        Обновлена будет запись, у которой getattr(schema, attr) == getattr(record, attr).

        При partial=False запись будет перезаписана полностью.
        При partial=True у записи останутся те поля, в которых у schema стоит None.

        Возвращает всю запись.
        """
        try:
            stmt = (
                sa.update(self.model)
                .filter_by(**{attr: getattr(schema, attr)})
                .values(**schema.dict(exclude_none=partial))
                .returning(self.model)
            )

            res = await self.session.execute(stmt)
            await self.session.commit()

            return res.scalar_one()

        except AttributeError:
            raise NotFoundError(detail={"msg": "No such attribute", "params": {"attribute_key": attr}})
        except sa.exc.NoResultFound:
            raise NotFoundError(detail={"msg": "No such record", "params": {attr: getattr(schema, attr)}})
