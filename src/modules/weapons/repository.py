from src.common.json_repository import JsonRepository
from src.modules.weapons.model import Weapon, WeaponSimple


class WeaponRepository(JsonRepository[WeaponSimple, Weapon]):
    def __init__(self) -> None:
        super().__init__(filename="weapons", model=Weapon, simple_model=WeaponSimple)
