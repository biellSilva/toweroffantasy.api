from src.domain.models.outfits import Outfit
from src.domain.usecases.outfits.find import FindOutfitsParams, IFindOutfitsUseCase


class FindOutfitsController:
    def __init__(self, usecase: IFindOutfitsUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> Outfit:
        return await self.usecase.execute(
            FindOutfitsParams(id=id, version=version, lang=lang)
        )
