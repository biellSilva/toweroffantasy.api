
import fastapi
import uvicorn

from typing import Callable, Any
from time import time as timer

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

DESC = ('[Interactive documentation](https://api.toweroffantasy.info/docs)\n\n'
        '[Detailed documentation](https://api.toweroffantasy.info/redoc)\n\n'
        '[Github](https://github.com/biellSilva/toweroffantasy.api)\n\n'
        '[GraphQL Docs](https://api.toweroffantasy.info/)\n\n\n'
        'If you find bugs, issues or want to tell us something, use the Github features like Issues or Discussions\n\n'
        '**HIGHLY RECOMMENDED TO USE DETAILED DOCS TO LEARN HOW THE API WORKS**')


app = FastAPI(title='Tower of Fantasy API',
              openapi_tags=TAGS_METADATA,
              description=DESC,
              version='1.1.3',
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
        raw = request.scope["query_string"].decode('latin-1').lower()
        request.scope["query_string"] = raw.encode('latin-1')

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