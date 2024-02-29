from src.domain.models.simulacra import Simulacra
from src.domain.usecases.simulacra.getall import (
    GetallSimulacraParams,
    IGetallSimulacraUseCase,
)
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class GetallSimulacraController:
    def __init__(self, usecase: IGetallSimulacraUseCase):
        self.usecase = usecase

    async def handle(
        self,
        version: VERSIONS_ENUM = VERSIONS_ENUM("global"),
        lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM = LANGS_GLOBAL_ENUM("en"),
    ) -> list[Simulacra]:
        return await self.usecase.execute(
            GetallSimulacraParams(version=version, lang=lang)
        )
