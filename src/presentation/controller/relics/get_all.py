from src.domain.models.relics import Relic
from src.domain.usecases.relics.get_all import GetAllRelicsParams, IGetAllRelicsUseCase


class GetAllRelicsController:
    def __init__(self, usecase: IGetAllRelicsUseCase):
        self.usecase = usecase

    async def handle(self, version: str = "global", lang: str = "en") -> list[Relic]:
        return await self.usecase.execute(
            GetAllRelicsParams(version=version, lang=lang)
        )
