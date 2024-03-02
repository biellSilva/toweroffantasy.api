from typing import Annotated

import strawberry
from pydantic import AliasChoices, BaseModel, BeforeValidator, Field

from src.utils import bold_numbers, string_or_null
from src.utils.weapon import weapon_effect_title


class ShatterOrCharge(BaseModel):
    value: float
    tier: str


class WeaponAssets(BaseModel):
    icon: str | None
    weaponIconForMatrix: str | None
    characterArtwork: str | None = None


class UpgradeMaterial(BaseModel):
    matId: Annotated[
        str | None,
        BeforeValidator(string_or_null),
    ] = Field(validation_alias=AliasChoices("mat_id", "matId"))
    amount: int | None = Field(validation_alias=AliasChoices("mat_amount", "amount"))
    name: str | None = None
    icon: str | None = None
    type: str | None = None
    description: str | None = None
    rarity: int | None = None


class LevelUpgrade(BaseModel):
    requiredExp: int
    mats: list[UpgradeMaterial]


class WeaponMats(BaseModel):
    id: str
    levels: list[LevelUpgrade]


class WeaponEffect(BaseModel):
    title: Annotated[
        str,
        BeforeValidator(weapon_effect_title),
    ]
    description: str


class Skill(BaseModel):
    name: str | None
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    values: list[list[float]] = []
    icon: str | None
    tags: list[str] = []
    operations: list[str] = []
    id: str | None


class WeaponAttacks(BaseModel):
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]


class AdvancMultipliers(BaseModel):
    statId: str = Field(validation_alias=AliasChoices("PropName", "id", "statId"))
    coefficient: float = Field(
        validation_alias=AliasChoices("PropCoefficient", "coefficient")
    )


class WeaponAdvancement(BaseModel):
    description: str | None = None
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    need: str | None
    multiplier: list[AdvancMultipliers]


class BaseStats(BaseModel):
    id: str
    name: str
    icon: str | None
    value: float = Field(0, validation_alias=AliasChoices("PropValue", "value"))
    upgradeProp: float = Field(validation_alias=AliasChoices("upgradeProp"))


@strawberry.experimental.pydantic.type(model=ShatterOrCharge, all_fields=True)
class ShatterOrChargeType:
    pass


@strawberry.experimental.pydantic.type(model=WeaponAssets, all_fields=True)
class WeaponAssetsType:
    pass


@strawberry.experimental.pydantic.type(model=UpgradeMaterial, all_fields=True)
class UpgradeMaterialType:
    pass


@strawberry.experimental.pydantic.type(model=LevelUpgrade, all_fields=True)
class LevelUpgradeType:
    pass


@strawberry.experimental.pydantic.type(model=WeaponMats, all_fields=True)
class WeaponMatsType:
    pass


@strawberry.experimental.pydantic.type(model=WeaponEffect, all_fields=True)
class WeaponEffectType:
    pass


@strawberry.experimental.pydantic.type(model=Skill, all_fields=True)
class SkillType:
    pass


@strawberry.experimental.pydantic.type(model=WeaponAttacks, all_fields=True)
class WeaponAttacksType:
    pass


@strawberry.experimental.pydantic.type(model=AdvancMultipliers, all_fields=True)
class AdvancMultipliersType:
    pass


@strawberry.experimental.pydantic.type(model=WeaponAdvancement, all_fields=True)
class WeaponAdvancementType:
    pass


@strawberry.experimental.pydantic.type(model=BaseStats, all_fields=True)
class BaseStatsType:
    pass
