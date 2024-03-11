from src.domain.models.outfits import Outfit
from src.domain.usecases.outfits.get_all import (
    GetAllOutfitsParams,
    IGetAllOutfitsUseCase,
)


class GetAllOutfitsController:
    def __init__(self, usecase: IGetAllOutfitsUseCase):
        self.usecase = usecase

    async def handle(self, version: str = "global", lang: str = "en") -> list[Outfit]:
        return await self.usecase.execute(
            GetAllOutfitsParams(version=version, lang=lang)
        )
