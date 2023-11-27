
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import replace_icon


class ListKeys(BaseModel):
    Time: float
    Value: float


class Assets(BaseModel):
    ItemIcon: str | None
    ItemLargeIcon: str | None
    WeaponUPIcon: str | None
    WeaponIconForMatrix: str | None
    LotteryCardImage: str | None
    SoloLeagueBanPickBanner: str | None


class Skill(BaseModel):
    Name: str | None
    Description: str | None
    Values: list[list[ListKeys]] = []
    ShortDesc: str | None
    Icon: str | None
    Tags: list[str]
    Operations: list[str]


class WeaponSkills(BaseModel):
    Name: str | None
    Description: str | None
    Icon: str | None
    Attacks: list[Skill]


class WeaponAttacks(BaseModel):
    Melee: WeaponSkills
    Evade: WeaponSkills
    Skill: WeaponSkills
    Discharge: WeaponSkills


class WeaponAdvancement(BaseModel):
    Description: str | None
    GoldNeeded: int 
    Shatter: float
    Charge: float
    NeedItem: str | None
    WeaponFashionID: str | None


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