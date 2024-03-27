from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, PositiveInt, StringConstraints
from pydantic_extra_types.country import CountryAlpha2

from src.core.constants import Gender

str_100_meta = StringConstraints(min_length=1, max_length=100, strip_whitespace=True, to_lower=True)


class InlineEmail(BaseModel):
    """Inline-модель, возвращаемая при получении списка Email пользователя."""

    id: UUID
    address: EmailStr


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


class UserSchemaAdditionalMixin(BaseModel):
    """Mixin для всех моделей с дополнительными полями возраст, пол, код страны."""

    age: PositiveInt | None = None
    gender: Gender
    country_code: CountryAlpha2 | None = None


class UserSchemaGetShort(UserSchemaUUIDMixin, UserSchemaOrmMixin, UserSchemaFullnameMixin):
    """Схема, возвращаемая при получении списка всех пользователей."""

    pass


class UserSchemaGet(UserSchemaUUIDMixin, UserSchemaOrmMixin, UserSchemaFullnameMixin, UserSchemaAdditionalMixin):
    """Схема, возвращаемая при получении подробной информации о пользователе."""

    emails: list[InlineEmail]


class UserSchemaPost(UserSchemaOrmMixin, UserSchemaFullnameMixin, UserSchemaAdditionalMixin):
    """Схема, отправляемая при создании пользователя."""

    pass


class UserSchemaUpdate(UserSchemaUUIDMixin, UserSchemaOrmMixin, UserSchemaFullnameMixin, UserSchemaAdditionalMixin):
    """Схема, получаемая при изменении пользователя."""

    pass
