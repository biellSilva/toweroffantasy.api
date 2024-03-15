from src.domain.models.researchs import Research
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.researchs.get_all import IGetAllResearchsUseCase


class GetAllResearchsController:
    def __init__(self, usecase: IGetAllResearchsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[Research]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
