from pydantic import BaseModel, BeforeValidator, Field, AliasChoices
from typing import Annotated

from api.utils import classify_rework, bold_numbers


class ListKeys(BaseModel):
    Time: float
    Value: float


class Assets(BaseModel):
    icon: str | None
    # itemLargeIcon: str | None
    # WeaponUPIcon: str | None
    weaponIconForMatrix: str | None
    characterArtwork: str | None = None


class Skill(BaseModel):
    name: str | None
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    values: list[list[float | int]] = []
    icon: str | None
    tags: list[str] = []
    operations: list[str] = []
    id: str | None


class WeaponSkills(BaseModel):
    Name: str | None
    Description: str | None
    Icon: str | None
    Attacks: list[Skill]


class WeaponAttacks(BaseModel):
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]


class ShatterOrCharge(BaseModel):
    value: float
    tier: str


class AdvancMultipliers(BaseModel):
    statId: str = Field(validation_alias=AliasChoices("PropName", "id", "statId"))
    coefficient: float = Field(
        validation_alias=AliasChoices("PropCoefficient", "coefficient")
    )


class WeaponAdvancement(BaseModel):
    description: str | None = None
    # GoldNeeded: int
    shatter: Annotated[ShatterOrCharge, BeforeValidator(lambda x: x if isinstance(x, dict) else classify_rework(x))]  # type: ignore
    charge: Annotated[ShatterOrCharge, BeforeValidator(lambda x: x if isinstance(x, dict) else classify_rework(x))]  # type: ignore
    need: str | None
    multiplier: list[AdvancMultipliers]
    # WeaponFashionID: str | None


class FashionWeaponInfo(BaseModel):
    FashionName: str
    FashionImitationId: str


class MatrixSuit(BaseModel):
    MatrixSuitName: str
    MatrixSuitDes: str


class WeaponEffect(BaseModel):
    title: Annotated[
        str,
        BeforeValidator(
            lambda x: (
                str(x).replace(":", "").replace("*", "")
                if x and str(x).endswith(":")
                else x
            )
        ),
    ]
    description: str


class BaseStats(BaseModel):
    id: str
    name: str
    icon: str | None
    value: float = Field(0, validation_alias=AliasChoices("PropValue", "value"))
    upgradeProp: float = Field(validation_alias=AliasChoices("upgradeProp"))


class UpgradeMaterial(BaseModel):
    id: str
    need: int | None
