from src.domain.models.guidebook import GuideBook
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.guidebooks.get_all import IGetAllGuidebooksUseCase


class GetAllGuidebooksController:
    def __init__(self, usecase: IGetAllGuidebooksUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[GuideBook]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
