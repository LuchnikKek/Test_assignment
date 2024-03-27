from src.models.emails import EmailsOrm
from src.utils.repository import SQLAlchemyRepository


class EmailsRepository(SQLAlchemyRepository):
    model = EmailsOrm
