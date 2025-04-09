from typing import TYPE_CHECKING

from src.common.mongo_repository import MongoRepository
from src.modules.weapons.model import Weapon, WeaponSimple

if TYPE_CHECKING:
    from src.modules.weapons.dtos import GetWeapon, GetWeapons


class WeaponRepository(MongoRepository[WeaponSimple, Weapon]):
    def __init__(self) -> None:
        super().__init__("weapons", WeaponSimple, Weapon)
        self.view = self._db.get_collection("WeaponsView")

    async def get_weapon(self, params: "GetWeapon") -> Weapon | None:
        """Get a Weapon by ID."""
        if data := await self.view.find_one(
            filter={"id": {"$regex": params.weapon_id, "$options": "i"}},
        ):
            return self._complex_model.model_validate(
                data,
                context={"lang": params.lang},
            )
        return None

    async def get_weapons(self, params: "GetWeapons") -> list[WeaponSimple]:
        """Get all Weapons."""
        return [
            self._simple_model.model_validate(document, context={"lang": params.lang})
            async for document in self.view.find(
                filter={},
                sort=[
                    ("position", -1),
                    ("is_limited", -1),
                    ("rarity", -1),
                ],
                skip=(params.page - 1) * params.limit,
                limit=params.limit,
            )
        ]
