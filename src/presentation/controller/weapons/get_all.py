from src.domain.models.weapons import Weapon
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.weapons.get_all import IGetAllWeaponsUseCase


class GetAllWeaponsController:
    def __init__(self, usecase: IGetAllWeaponsUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str | None = None
    ) -> list[Weapon]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter)
        )
