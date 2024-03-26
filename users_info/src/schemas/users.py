from uuid import UUID

from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.country import CountryAlpha2

from src.core.constants import Gender


class UserSchemaOutShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    firstname: str
    lastname: str
    patronymic: str | None


class UserSchemaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    firstname: str
    lastname: str
    patronymic: str | None
    age: int | None
    country_code: CountryAlpha2 | None
    gender: Gender
