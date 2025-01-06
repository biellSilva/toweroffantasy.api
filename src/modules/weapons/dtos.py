from typing import Annotated

from fastapi import Path

from src.modules.base.dtos import BaseDataDto


class GetWeapon(BaseDataDto):
    weapon_id: Annotated[str, Path(description="Weapon id")]
