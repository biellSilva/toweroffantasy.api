from fastapi import FastAPI

from src._lifespan import lifespan
from src._settings import config


def create_app() -> FastAPI:
    return FastAPI(
        title=config.PROJECT_NAME,
        lifespan=lifespan,
        exception_handlers={ApiError: ApiError.handle_error},
    )
