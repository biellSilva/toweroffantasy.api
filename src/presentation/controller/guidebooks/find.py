from src.domain.models.guidebook import GuideBook
from src.domain.usecases.guidebooks.find import (
    FindGuidebooksParams,
    IFindGuidebooksUseCase,
)


class FindGuidebooksController:
    def __init__(self, usecase: IFindGuidebooksUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> GuideBook:
        return await self.usecase.execute(
            FindGuidebooksParams(id=id, version=version, lang=lang)
        )
