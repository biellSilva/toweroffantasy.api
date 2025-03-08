from src.modules._utils import rarity_to_int
from src.modules.base.json_repository import JsonRepository
from src.modules.weapons.model import Weapon, WeaponSimple


class WeaponRepository(JsonRepository[Weapon, WeaponSimple]):
    def __init__(self) -> None:
        super().__init__(name="weapons", model=Weapon, simple_model=WeaponSimple)

    async def get_all(self, *, lang: str) -> list[WeaponSimple]:
        return sorted(
            await super().get_all(lang=lang),
            key=lambda x: (-x.is_limited, -rarity_to_int(x.rarity), x.name),
        )
