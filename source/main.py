from fastapi import FastAPI

from source.router import router

application = FastAPI(
    title='Тестовый REST'
)

application.include_router(router)