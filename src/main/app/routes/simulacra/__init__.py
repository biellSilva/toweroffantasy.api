from fastapi import APIRouter

from src.main.factories.controller.simulacra.find import FindSimulacraControllerFactory
from src.main.factories.controller.simulacra.getall import (
    GetallSimulacraControllerFactory,
)

router = APIRouter(prefix="/simulacra", tags=["Simulacra"])

find = FindSimulacraControllerFactory.create()
get_all = GetallSimulacraControllerFactory.create()

router.add_api_route(
    path="/{id}", endpoint=find.handle, methods=["GET"], name="Find simulacrum"
)

router.add_api_route(
    path="", endpoint=get_all.handle, methods=["GET"], name="Get simulacra"
)
