from src.domain.models.weapons import Weapon
from src.domain.usecases.weapons.get_all import (
    GetAllWeaponsParams,
    IGetAllWeaponsUseCase,
)


class GetAllWeaponsController:
    def __init__(self, usecase: IGetAllWeaponsUseCase):
        self.usecase = usecase

    async def handle(self, version: str = 'global', lang: str = 'en') -> list[Weapon]:
        return await self.usecase.execute(
            GetAllWeaponsParams(version=version, lang=lang)
        )