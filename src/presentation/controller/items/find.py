from src.domain.models.items import Item
from src.domain.usecases.items.find import FindItemsParams, IFindItemsUseCase


class FindItemsController:
    def __init__(self, usecase: IFindItemsUseCase):
        self.usecase = usecase

    async def handle(self, id: str, version: str = "global", lang: str = "en") -> Item:
        return await self.usecase.execute(
            FindItemsParams(id=id, version=version, lang=lang)
        )
