from fastapi import FastAPI

from src._settings import config


def create_app() -> FastAPI:
    return FastAPI(
        title=config.PROJECT_NAME,
    )
