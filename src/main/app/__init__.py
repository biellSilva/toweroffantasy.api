from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import config
from src.main.app.routes import graphql
from src.presentation.middlewares.timer import ProcessTimerMiddleware

app = FastAPI(
    title=config.PROJECT_NAME,
    description=config.PROJECT_DESC,
    version=config.PROJECT_VERSION,
    license_info=config.PROJECT_LICENSE,
    summary=config.PROJECT_SUMMARY,
    swagger_ui_parameters=config.SWAGGER_UI_PARAMS,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ProcessTimerMiddleware)

app.include_router(router=graphql.router, tags=['Graphql'])
app.add_websocket_route(path='/graphql', route=graphql.router) # type: ignore