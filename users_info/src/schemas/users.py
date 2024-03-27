from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, PositiveInt, StringConstraints
from pydantic_extra_types.country import CountryAlpha2

from src.core.constants import Gender

str_100_meta = StringConstraints(min_length=1, max_length=100, strip_whitespace=True, to_lower=True)


class UserSchemaUUIDMixin(BaseModel):
    """Mixin для всех моделей с UUID."""

    id: UUID


class UserSchemaOrmMixin(BaseModel):
    """Mixin для всех моделей с ConfigDict."""

    model_config = ConfigDict(from_attributes=True)


class UserSchemaFullnameMixin(BaseModel):
    """Mixin для всех моделей с ФИО."""

    firstname: Annotated[str, str_100_meta]
    lastname: Annotated[str, str_100_meta]
    patronymic: Annotated[str | None, str_100_meta] = None


class UserSchemaOptionalMixin(BaseModel):
    """Mixin для всех моделей с необязательными полями возраст, пол, код страны."""

    age: PositiveInt | None = None
    gender: Gender
    country_code: CountryAlpha2 | None = None


class UserSchemaShort(UserSchemaUUIDMixin, UserSchemaOrmMixin, UserSchemaFullnameMixin):
    """Пользователь с UUID, ConfigDict и полями имени."""

    pass


class UserSchemaFull(UserSchemaUUIDMixin, UserSchemaOrmMixin, UserSchemaFullnameMixin, UserSchemaOptionalMixin):
    """Пользователь с UUID, ConfigDict, полями имени и дополнительной информацией."""

    pass


class UserSchemaFullPost(UserSchemaOrmMixin, UserSchemaFullnameMixin, UserSchemaOptionalMixin):
    """Пользователь с ConfigDict, полями имени и дополнительной информацией"""

    pass
