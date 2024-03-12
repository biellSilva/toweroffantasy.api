import json

from src.domain.models.items import Item
from src.domain.usecases.items.get_all import GetAllItemsParams, IGetAllItemsUseCase


class GetAllItemsController:
    def __init__(self, usecase: IGetAllItemsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str = ""
    ) -> list[Item]:
        return await self.usecase.execute(
            GetAllItemsParams(
                version=version, lang=lang, filter=json.loads(filter) if filter else {}
            )
        )
