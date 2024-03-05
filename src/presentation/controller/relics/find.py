from src.domain.models.relics import Relic
from src.domain.usecases.relics.find import FindRelicsParams, IFindRelicsUseCase


class FindRelicsController:
    def __init__(self, usecase: IFindRelicsUseCase):
        self.usecase = usecase

    async def handle(self, id: str, version: str = "global", lang: str = "en") -> Relic:
        return await self.usecase.execute(
            FindRelicsParams(id=id, version=version, lang=lang)
        )
