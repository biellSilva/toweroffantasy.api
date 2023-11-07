
from fastapi import FastAPI

from api.routes import (
    simulacra, 
    simulacra_v2, 
    names,
    weapons,
    matrices,
    relics,
    home
)


app = FastAPI()

app.include_router(home.router)
app.include_router(simulacra.router)
app.include_router(simulacra_v2.router)
app.include_router(weapons.router)
app.include_router(matrices.router)
app.include_router(relics.router)
app.include_router(names.router)

