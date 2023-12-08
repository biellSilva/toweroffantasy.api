
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import replace_icon


class ListKeys(BaseModel):
    Time: float
    Value: float


class Assets(BaseModel):
    icon: str | None
    # itemLargeIcon: str | None
    # WeaponUPIcon: str | None
    weaponIconForMatrix: str | None


class Skill(BaseModel):
    name: str | None
    description: str | None
    # Values: list[list[ListKeys]] = []
    icon: str | None
    tags: list[str] = []
    operations: list[str] = []


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


class WeaponAdvancement(BaseModel):
    description: str | None = None
    # GoldNeeded: int 
    shatter: float
    charge: float
    need: str | None
    # WeaponFashionID: str | None


class FashionWeaponInfo(BaseModel):
    FashionName: str
    FashionImitationId: str


class MatrixSuit(BaseModel):
    MatrixSuitName: str
    MatrixSuitDes: str


class WeaponEffect(BaseModel):
    title: str
    description: str


class ShatterOrCharge(BaseModel):
    value: float
    tier: str


class RecoMatrix(BaseModel):
    id: str
    pieces: int


class MetaData(BaseModel):
    recommendedPairings: list[str] = []
    recommendedMatrices: list[RecoMatrix] = []
    rating: list[int] = []
    analyticVideoId: str | None = None


class BaseStats(BaseModel):
    id: str
    name: str
    icon: Annotated[str, BeforeValidator(replace_icon)]


class UpgradeMaterial(BaseModel):
    id: str
    need: int | None