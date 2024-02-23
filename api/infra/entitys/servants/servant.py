from pydantic import Field

from api.infra.entitys.base import EntityBase

from .extra import ServantAsset, ServantSkill, ServantUpgrade


class SmartServant(EntityBase):
    name: str
    description: str
    rarity: int = Field(validation_alias="petRarity")
    element: str = Field(validation_alias="petElementType")
    type: str = Field(validation_alias="petPropertyType")
    assets: ServantAsset
    skills: list[ServantSkill]
    upgradeItems: list[ServantUpgrade] = Field(validation_alias="petUpgradeItemMap")
