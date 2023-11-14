
from fastapi import FastAPI, Request, Response
from typing import Callable, Any
from time import time as timer

from api.core.routes import (
    simulacra, 
    simulacra_v2, 
    weapons,
    matrices,
    relics,
    # home,
    food,
    item,
    achievements,
    outfits,
    image,
    graphql
)


app = FastAPI()

# app.include_router(home.router)
app.include_router(simulacra.router)
app.include_router(simulacra_v2.router)
app.include_router(weapons.router)
app.include_router(matrices.router)
app.include_router(relics.router)
app.include_router(food.router)
app.include_router(item.router)
app.include_router(achievements.router)
app.include_router(outfits.router)
app.include_router(image.router)

app.include_router(graphql.graphql, tags=['GraphQL']) # type: ignore


@app.middleware("http")
@app.middleware("https")
async def add_process_time_header(request: Request, call_next: Callable[[Request], Any]):
    start_time = timer()
    response: Response = await call_next(request)
    response.headers["X-Process-Time"] = str(timer() - start_time)
    return response

