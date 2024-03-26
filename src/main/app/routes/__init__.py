from fastapi import APIRouter

from src.main.app.routes import docs

from . import assets, graphql, simulacra

router = APIRouter(prefix="")

router.include_router(router=graphql.router, tags=["Graphql"], include_in_schema=False)
router.add_websocket_route(path="/graphql", endpoint=graphql.router)  # type: ignore

router.include_router(router=simulacra.router)

router.include_router(router=assets.router)
router.include_router(router=docs.router)
