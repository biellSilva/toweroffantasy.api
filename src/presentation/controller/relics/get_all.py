from src.domain.models.relics import Relic
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.relics.get_all import IGetAllRelicsUseCase


class GetAllRelicsController:
    def __init__(self, usecase: IGetAllRelicsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[Relic]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
