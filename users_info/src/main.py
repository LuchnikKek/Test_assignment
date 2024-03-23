from fastapi import FastAPI
from src.api.routers import all_routers


app = FastAPI(title="Личный кабинет пользователя")


for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", reload=True)
