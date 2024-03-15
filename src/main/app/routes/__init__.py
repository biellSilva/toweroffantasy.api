from fastapi import APIRouter

from . import assets, graphql, simulacra

router = APIRouter(prefix="")

router.include_router(router=graphql.router, tags=["Graphql"])
router.add_websocket_route(path="/graphql", endpoint=graphql.router)  # type: ignore

router.include_router(router=simulacra.router)

router.include_router(router=assets.router)
