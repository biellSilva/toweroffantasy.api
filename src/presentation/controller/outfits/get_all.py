from src.domain.models.outfits import Outfit
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.outfits.get_all import IGetAllOutfitsUseCase


class GetAllOutfitsController:
    def __init__(self, usecase: IGetAllOutfitsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[Outfit]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
