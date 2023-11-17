
from pydantic import Field

from api.infra.entitys.base import EntityBase

from .extra import ServantAsset, ServantSkill, ServantUpgrade


class SmartServant(EntityBase):
    name: str
    description: str
    rarity: str = Field(alias='PetRarity', serialization_alias='rarity')
    element: str = Field(alias='PetElementType', serialization_alias='element')
    type: str = Field(alias='PetPropertyType', serialization_alias='type')
    assets: ServantAsset
    skills: list[ServantSkill]
    upgradeItems: list[ServantUpgrade]