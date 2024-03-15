from src.domain.models.items import Item
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.items.get_all import IGetAllItemsUseCase


class GetAllItemsController:
    def __init__(self, usecase: IGetAllItemsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[Item]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
