import strawberry
from pydantic import BaseModel, Field


class ServantAsset(BaseModel):
    petIcon: str | None = Field(validation_alias="petIcon")
    activatedIcon: str | None = Field(validation_alias="petActivatedIcon")
    itemIcon: str | None = Field(validation_alias="itemIcon")


class ServantSkill(BaseModel):
    name: str
    description: str
    icon: str | None


class ServantUpgradeMaterial(BaseModel):
    id: str
    name: str
    description: str
    rarity: int
    icon: str
    type: str


class ServantUpgrade(BaseModel):
    material: ServantUpgradeMaterial
    exp: int


class ServantAdvanceMat(BaseModel):
    id: str
    name: str
    description: str
    icon: str
    rarity: int
    type: str
    amount: int = Field(validation_alias="mat_amount")


class ServantAdvancement(BaseModel):
    description: str
    mats: list[ServantAdvanceMat]


@strawberry.experimental.pydantic.type(model=ServantAdvanceMat, all_fields=True)
class ServantAdvanceMatType:
    pass


@strawberry.experimental.pydantic.type(model=ServantAdvancement, all_fields=True)
class ServantAdvancementType:
    pass


@strawberry.experimental.pydantic.type(model=ServantAsset, all_fields=True)
class ServantAssetType:
    pass


@strawberry.experimental.pydantic.type(model=ServantSkill, all_fields=True)
class ServantSkillType:
    pass


@strawberry.experimental.pydantic.type(model=ServantUpgradeMaterial, all_fields=True)
class ServantUpgradeMaterialType:
    pass


@strawberry.experimental.pydantic.type(model=ServantUpgrade, all_fields=True)
class ServantUpgradeType:
    pass
