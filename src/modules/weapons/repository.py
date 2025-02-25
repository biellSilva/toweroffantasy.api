from src.modules.base.json_repository import JsonRepository
from src.modules.weapons.model import Weapon, WeaponSimple


class WeaponRepository(JsonRepository[Weapon, WeaponSimple]):
    def __init__(self) -> None:
        super().__init__(name="weapons", model=Weapon, simple_model=WeaponSimple)
