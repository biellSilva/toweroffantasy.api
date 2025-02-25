from fastapi import FastAPI

from src._lifespan import lifespan
from src._settings import config
from src._version import get_version
from src.exceptions.base import ApiError


def create_app() -> FastAPI:
    app = FastAPI(
        title=config.PROJECT_NAME,
        summary=config.project_summary,
        description=config.project_description,
        lifespan=lifespan,
        exception_handlers={ApiError: ApiError.handle_error},
        version=get_version(),
    )

    add_routes(app)

    return app


def add_routes(app: FastAPI) -> None:
    from src.modules.router import router

    app.include_router(router)


def add_middlewares(app: FastAPI) -> None:
    from src.middlewares.timeit import ProcessTime

    app.add_middleware(ProcessTime)
