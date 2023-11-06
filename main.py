
from fastapi import FastAPI
from uvicorn import run # type: ignore

from api.routes import simulacra

app = FastAPI()

app.include_router(simulacra.router)


if __name__ == '__main__':
    run(app='main:app', access_log=False, reload=True, reload_delay=5, workers=1)