

from typing import Callable, Any
from time import time as timer

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from slowapi import Limiter, _rate_limit_exceeded_handler # type: ignore
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware


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
    raritys,
    image,
    graphql,
)


app = FastAPI()

limiter = Limiter(key_func=get_remote_address, application_limits=['1/10seconds'], enabled=False)
app.state.limiter = limiter

app.add_middleware(SlowAPIMiddleware)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler) # type: ignore

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.middleware("http")
@app.middleware("https")
async def add_process_time_header(request: Request, call_next: Callable[[Request], Any]):
    start_time = timer()
    response: Response = await call_next(request)
    response.headers["X-Process-Time"] = str(timer() - start_time)
    return response

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
app.include_router(raritys.router)
app.include_router(image.router)

app.include_router(graphql.graphql, tags=['GraphQL']) # type: ignore
