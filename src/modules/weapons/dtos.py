from typing import Annotated

from fastapi import Path

from src.modules.base.dtos import BaseSearchDto


class GetWeapon(BaseSearchDto):
    weapon_id: Annotated[str, Path(description="Weapon id")]
