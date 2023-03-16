from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.handlers import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application

app = get_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)