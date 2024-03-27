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
            user1 = res1.unique.scalars().one()
            user2 = res2.unique.scalars().one()
            user2.friend_requests.append(user1)
            user1.friend_accepts.append(user2)
        except sa.exc.NoResultFound:
            raise NotFoundError(
                detail={
                    "msg": "Not found",
                    "params": {"req_user_id": str(data.request_user_id), "accept_user_id": str(data.accept_user_id)},
                }
            )
        await self.session.commit()
        return
