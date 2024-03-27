from typing import Annotated

from pydantic import EmailStr
from pydantic_extra_types.country import CountryAlpha2
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.core.config import settings

str_100 = Annotated[str, 100]
country_alpha_2 = Annotated[CountryAlpha2, 2]
email = Annotated[EmailStr, 100]


class Base(DeclarativeBase):
    """
    Декларативный базовый класс для наследования моделей SQLAlchemy.

    Attributes:
        `repr_cols_num`: int. Количество столбцов в методе `__repr__()`.
        `repr_cols`: tuple(str). Дополнительные выводимые столбцы в методе `__repr__()`.
    """

    type_annotation_map = {str_100: String(100), country_alpha_2: String(2), email: String(100)}

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self) -> str:
        """
        Возвращает формальное представление объекта.

        Возвращаемые поля можно настраивать, перезаписывая у модели значения `repr_cols_num` и `repr_cols`.

        Returns:
            Строку, содержащую первые `repr_cols_num` столбцов **И** все столбцы, перечисленные в `repr_cols`.
            Лишние `repr_cols_num` и `repr_cols` будут проигнорированы.

            Формат вывода:
            '<Модель [столбец 1]=[значение 1], ..., [столбец repr_cols_num]=[значение repr_cols_num]>'  # noqa
        """
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"


engine = create_async_engine(
    url=settings.database.dsn,
    echo=settings.debug,
)

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    """Возвращает асинхронную сессию. Автоматически закрывает её."""
    async with async_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
