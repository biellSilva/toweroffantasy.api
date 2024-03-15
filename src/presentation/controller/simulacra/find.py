from fastapi import Depends

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.base import FindParams
from src.domain.usecases.simulacra.find import IFindSimulacraUseCase


class FindSimulacraController:
    def __init__(self, usecase: IFindSimulacraUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> Simulacra:

        return await self.usecase.execute(FindParams(id=id, version=version, lang=lang))

    async def rest_handle(self, params: FindParams = Depends()) -> Simulacra:
        return await self.usecase.execute(params)
