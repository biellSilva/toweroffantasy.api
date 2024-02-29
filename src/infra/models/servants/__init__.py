from pydantic import Field

from src.domain.models.base import ModelBase

from .extras import ServantAsset, ServantSkill, ServantUpgrade


class SmartServant(ModelBase):
    name: str
    description: str
    rarity: int = Field(validation_alias="petRarity")
    element: str = Field(validation_alias="petElementType")
    type: str = Field(validation_alias="petPropertyType")
    assets: ServantAsset
    skills: list[ServantSkill]
    upgradeItems: list[ServantUpgrade] = Field(validation_alias="petUpgradeItemMap")
    properties: str
    advancements: list[str]
