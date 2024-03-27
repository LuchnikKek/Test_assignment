import logging

import sqlalchemy as sa
from pydantic import BaseModel

from src.core.exceptions import NotFoundError
from src.models import UsersOrm
from src.utils.repository import SQLAlchemyRepository


class FriendsRepository(SQLAlchemyRepository):
    model = UsersOrm

    async def add_one(self, data: BaseModel):
        stmt1 = sa.select(self.model).filter_by(**{"id": str(data.request_user_id)})
        stmt2 = sa.select(self.model).filter_by(**{"id": str(data.accept_user_id)})

        res1 = await self.session.execute(stmt1)
        res2 = await self.session.execute(stmt2)

        try:
            user1: UsersOrm = res1.unique().scalars().one()
            user2: UsersOrm = res2.unique().scalars().one()
            logging.critical(user1)
            logging.critical(user1)
            logging.critical(user1)
            logging.critical(user2)
            logging.critical(user2)
            logging.critical(user2)
            raise Exception
        except sa.exc.NoResultFound:
            raise NotFoundError(
                detail={
                    "msg": "Not found",
                    "params": {"req_user_id": str(data.request_user_id), "accept_user_id": str(data.accept_user_id)},
                }
            )

        # stmt = UsersOrm.friends.

        stmt = sa.insert(self.model).values(**data.dict()).returning(self.model.id)

        try:
            res = await self.session.execute(stmt)
        except sa.exc.IntegrityError:
            raise AlreadyExistsError(detail={"msg": "Record already exists"})

        await self.session.commit()
        return res.scalar_one()
