from typing import TYPE_CHECKING

from src._types import LangsEnum
from src.exceptions.not_found import WeaponNotFoundError
from src.modules.weapons.model import Weapon

if TYPE_CHECKING:
    from src.modules.weapons.repository import WeaponRepository


class WeaponService:
    def __init__(self, repository: "WeaponRepository") -> None:
        self.repository = repository

    async def get(self, *, lang: LangsEnum, _id: str) -> Weapon:
        if data := await self.repository.get_id(lang=lang, _id=_id):
            return Weapon(**data)
        raise WeaponNotFoundError(lang=lang, id=_id)

    async def get_all(self, *, lang: LangsEnum) -> list[Weapon]:
        return [Weapon(**data) for data in await self.repository.get_all(lang=lang)]
