from fastapi import APIRouter

from src.main.factories.controller.simulacra.find import FindSimulacraControllerFactory
from src.main.factories.controller.simulacra.getall import (
    GetallSimulacraControllerFactory,
)

router = APIRouter(prefix="/simulacra", tags=["Simulacra"])

router.add_api_route(
    path="/{id}",
    endpoint=FindSimulacraControllerFactory.create().rest_handle,
    methods=["GET"],
)

router.add_api_route(
    path="",
    endpoint=GetallSimulacraControllerFactory.create().rest_handle,
    methods=["GET"],
)
