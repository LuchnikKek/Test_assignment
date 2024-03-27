from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class EmailSchemaUUIDMixin(BaseModel):
    """Mixin для всех схем с UUID."""

    id: UUID


class EmailSchemaOrmMixin(BaseModel):
    """Mixin для всех схем с ConfigDict."""

    model_config = ConfigDict(from_attributes=True)


class EmailSchemaPost(EmailSchemaOrmMixin):
    """Схема, отправляемая при добавлении ящика электронной почты."""

    address: EmailStr
    user_id: UUID
