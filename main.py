
from fastapi import FastAPI
from uvicorn import run # type: ignore

from api.routes import simulacra

app = FastAPI()

app.include_router(simulacra.router)


if __name__ == '__main__':
    run(app=app, 
        access_log=False, 
        # reload=True,      # dev function
        # reload_delay=5,   # dev function
        # workers=1         # dev function
        )