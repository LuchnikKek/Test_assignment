from fastapi import APIRouter

from src.api.v1.emails import router as router_emails
from src.api.v1.users import router as router_users

routers = APIRouter()
routes = [router_users, router_emails]

for router in routes:
    routers.include_router(router)
