from fastapi import APIRouter

from src.main.factories.controller.simulacra.find import FindSimulacraControllerFactory

router = APIRouter(prefix="/simulacra", tags=["Simulacra"])

find = FindSimulacraControllerFactory.create()

router.add_api_route(
    path="/{id}", endpoint=find.handle, methods=["GET"], name="Find simulacrum"
)
