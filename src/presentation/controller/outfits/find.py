from src.domain.models.outfits import Outfit
from src.domain.usecases.base import FindParams
from src.domain.usecases.outfits.find import IFindOutfitsUseCase


class FindOutfitsController:
    def __init__(self, usecase: IFindOutfitsUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> Outfit:
        return await self.usecase.execute(FindParams(id=id, version=version, lang=lang))
