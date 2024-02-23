from src.domain.models.simulacra import Simulacra
from src.domain.usecases.simulacra.find import (
    FindSimulacraParams,
    IFindSimulacraUseCase,
)
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM
from src.enums.simulacra import SIMULACRAS_GLOBAL_ENUM


class FindSimulacraController:
    def __init__(self, usecase: IFindSimulacraUseCase):
        self.usecase = usecase

    async def handle(
        self,
        id: SIMULACRAS_GLOBAL_ENUM,
        version: VERSIONS_ENUM = VERSIONS_ENUM("global"),
        lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM = LANGS_GLOBAL_ENUM("en"),
    ) -> Simulacra:
        "Find simulacra based on ID"
        return await self.usecase.execute(
            FindSimulacraParams(id=id, version=version, lang=lang)
        )
