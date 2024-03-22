import uuid

from sqlalchemy import Column, UUID
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr

from users_info.src.core.config import settings


class PreBase(AsyncAttrs):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(UUID(), primary_key=True, default=uuid.uuid4)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(
    url=settings.postgres.dsn,
    echo=True,
)

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    async with async_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
