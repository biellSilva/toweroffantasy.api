from src.domain.models.researchs import Research
from src.domain.usecases.base import FindParams
from src.domain.usecases.researchs.find import IFindResearchsUseCase


class FindResearchsController:
    def __init__(self, usecase: IFindResearchsUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> Research:
        return await self.usecase.execute(FindParams(id=id, version=version, lang=lang))
