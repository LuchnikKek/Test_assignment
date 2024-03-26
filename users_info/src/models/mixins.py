import datetime
import uuid

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class UuidMixin(object):
    """Mixin, добавляющий модели UUID."""

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)


class CreatedMixin(object):
    """Mixin, добавляющий модели поле с датой создания."""

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class UpdatedMixin(object):
    """Mixin, добавляющий модели поле с датой изменения."""

    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now())


class TimestampedMixin(CreatedMixin, UpdatedMixin):
    """Mixin, добавляющий модели поля с датой создания и датой изменения."""

    pass
