
import fastapi
import uvicorn

from typing import Callable, Any
from time import time as timer
from datetime import datetime
from pytz import timezone

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from slowapi import Limiter, _rate_limit_exceeded_handler # type: ignore
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware


from api.routes import (
    extras,
    simulacra, 
    simulacra_v2, 
    weapons,
    matrices,
    relics,
    food,
    item,
    achievements,
    outfits,
    image,
    graphql,
    mounts,
    servants,
    home
)


print(f'''
FastAPI: {fastapi.__version__}
Uvicorn: {uvicorn.__version__}
''')


TAGS_METADATA = [
    simulacra.METADATA,
    weapons.METADATA,
    matrices.METADATA,
    simulacra_v2.METADATA,
    relics.METADATA,
    outfits.METADATA,
    mounts.METADATA,
    servants.METADATA,
    item.METADATA,
    food.METADATA,
    achievements.METADATA,

    extras.METADATA,
    image.METADATA,
    graphql.METADATA
]

LAST_RESTART = datetime.now(timezone("UTC"))

DESC = (
        '[Interactive docs](https://api.toweroffantasy.info/docs)\t\n'
        '[Detailed docs](https://api.toweroffantasy.info/redoc)\t\n'
        '[GraphQL docs](https://api.toweroffantasy.info/graphql)\t\n'
        '[Discord](https://discord.com/invite/aida-cafe-670617630717116426)\t\n'
        '[Github](https://github.com/biellSilva/toweroffantasy.api)\t\n'
        '\n'
        'Created by:\t\n'
            '- [biell (API side)](https://discord.com/users/420634633793699851)\t\n'
            '- [Emi (ToF Index)](https://discord.com/users/851815237120163840)\t\n'
            '- [FortOfFans (Data side)](https://discord.com/users/238308687373008898)\t\n'
            '- [Zakum (ToF Index)](https://discord.com/users/134492795133100033)\t\n'
        '\n'
        f'Last restart: {LAST_RESTART}' 
        )


app = FastAPI(title='Tower of Fantasy API',
              openapi_tags=TAGS_METADATA,
              description=DESC,
            )

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
async def process_request(request: Request, call_next: Callable[[Request], Any]):
    start_time = timer()
    
    if 'asset' not in request.url.path:
        path = request.scope["path"].lower()
        request.scope["path"] = path

    response: Response = await call_next(request)
    response.headers["X-Process-Time"] = str(timer() - start_time)
    return response


app.include_router(simulacra.router)
app.include_router(simulacra_v2.router)
app.include_router(weapons.router)
app.include_router(matrices.router)
app.include_router(relics.router)
app.include_router(food.router)
app.include_router(item.router)
app.include_router(achievements.router)
app.include_router(outfits.router)
app.include_router(mounts.router)
app.include_router(servants.router)
app.include_router(extras.router)
app.include_router(image.router)

app.include_router(home.router, include_in_schema=False)

app.include_router(graphql.graphql, tags=['GraphQL']) 
app.add_websocket_route('/graphql', graphql.graphql) # type: ignore  