import datetime
import uuid

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column


class UuidMixin(object):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)


class CreatedMixin(object):
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))


class UpdatedMixin(object):
    updated_at: Mapped[datetime.datetime] = mapped_column(onupdate=lambda: datetime.datetime.now(datetime.UTC))


class TimestampedMixin(CreatedMixin, UpdatedMixin):
    pass
