from src.domain.models.weapons import Weapon
from src.domain.usecases.weapons.find import FindWeaponsParams, IFindWeaponsUseCase


class FindWeaponsController:
    def __init__(self, usecase: IFindWeaponsUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str, version: str = "global", lang: str = "en"
    ) -> Weapon:
        return await self.usecase.execute(
            FindWeaponsParams(id=id, version=version, lang=lang)
        )
