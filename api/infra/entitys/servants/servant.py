
from pydantic import Field, BeforeValidator
from typing import Annotated

from api.infra.entitys.base import EntityBase
from .extra import ServantAsset, ServantSkill, ServantUpgrade

from api.utils import pet_material_rework


class SmartServant(EntityBase):
    name: str
    description: str
    rarity: str = Field(validation_alias='petRarity')
    element: str = Field(validation_alias='petElementType')
    type: str = Field(validation_alias='petPropertyType')
    assets: ServantAsset
    skills: list[ServantSkill]
    upgradeItems: Annotated[list[ServantUpgrade], BeforeValidator(pet_material_rework)] = Field(validation_alias='petUpgradeItemMap')