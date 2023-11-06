
from fastapi import FastAPI
from uvicorn import run # type: ignore

from api.routes import simulacra

app = FastAPI()

app.include_router(simulacra.router)


run(app=app, access_log=False)