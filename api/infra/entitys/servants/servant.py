
from pydantic import Field, BeforeValidator
from typing import Annotated

from api.infra.entitys.base import EntityBase
from .extra import ServantAsset, ServantSkill, ServantUpgrade

from api.utils import pet_material_rework


class SmartServant(EntityBase):
    name: str
    description: str
    rarity: str = Field(alias='PetRarity', serialization_alias='rarity')
    element: str = Field(alias='PetElementType', serialization_alias='element')
    type: str = Field(alias='PetPropertyType', serialization_alias='type')
    assets: ServantAsset
    skills: list[ServantSkill]
    upgradeItems: Annotated[list[ServantUpgrade], BeforeValidator(pet_material_rework)] = Field(alias='PetUpgradeItemMap', serialization_alias='upgradeItems')