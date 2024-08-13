from fastapi import FastAPI

from source.router import router

application = FastAPI()

application.include_router(router)