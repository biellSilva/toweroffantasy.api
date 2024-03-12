import json

from src.domain.models.guidebook import GuideBook
from src.domain.usecases.guidebooks.get_all import (
    GetAllGuidebooksParams,
    IGetAllGuidebooksUseCase,
)


class GetAllGuidebooksController:
    def __init__(self, usecase: IGetAllGuidebooksUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str = ""
    ) -> list[GuideBook]:
        return await self.usecase.execute(
            GetAllGuidebooksParams(
                version=version, lang=lang, filter=json.loads(filter) if filter else {}
            )
        )
