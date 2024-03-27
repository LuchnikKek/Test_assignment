from fastapi import APIRouter, Depends

from src.api.v1.dependencies import get_emails_service
from src.schemas.emails import EmailSchemaPost, EmailSchemaUUIDMixin
from src.services.emails import EmailsService

router = APIRouter(prefix="/emails", tags=["E-mails"])


@router.post("", response_model=EmailSchemaUUIDMixin)
async def post_email(
    email: EmailSchemaPost,
    emails_service: EmailsService = Depends(get_emails_service),
):
    """Создаёт новый адрес электронной почты."""
    return {"id": await emails_service.set(email)}
