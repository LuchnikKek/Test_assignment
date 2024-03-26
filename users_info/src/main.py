from fastapi import FastAPI
from src.api.routers import routers


app = FastAPI(title="Личный кабинет пользователя")
app.include_router(routers, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", reload=True)
