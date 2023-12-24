
from pydantic import BaseModel, BeforeValidator, Field, AliasChoices
from typing import Annotated

from api.utils import replace_icon, classify_rework, bold_numbers


class ListKeys(BaseModel):
    Time: float
    Value: float


class Assets(BaseModel):
    icon: Annotated[str | None, BeforeValidator(replace_icon)] 
    # itemLargeIcon: str | None
    # WeaponUPIcon: str | None
    weaponIconForMatrix: Annotated[str | None, BeforeValidator(replace_icon)] 
    characterArtwork: str | None = None


class Skill(BaseModel):
    name: str | None
    description: Annotated[str, BeforeValidator(bold_numbers)] | None
    values: list[list[float | int]] = []
    icon: Annotated[str | None, BeforeValidator(replace_icon)] 
    tags: list[str] = []
    operations: list[str] = []
    id: str | None


class WeaponSkills(BaseModel):
    Name: str | None
    Description: str | None
    Icon: Annotated[str | None, BeforeValidator(replace_icon)] 
    Attacks: list[Skill]


class WeaponAttacks(BaseModel):
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]


class ShatterOrCharge(BaseModel):
    value: float
    tier: str

class WeaponAdvancement(BaseModel):
    description: str | None = None
    # GoldNeeded: int 
    shatter: Annotated[ShatterOrCharge, BeforeValidator(lambda x: x if isinstance(x, dict) else classify_rework(x))]    # type: ignore
    charge: Annotated[ShatterOrCharge, BeforeValidator(lambda x: x if isinstance(x, dict) else classify_rework(x))]     # type: ignore
    need: str | None
    # WeaponFashionID: str | None


class FashionWeaponInfo(BaseModel):
    FashionName: str
    FashionImitationId: str


class MatrixSuit(BaseModel):
    MatrixSuitName: str
    MatrixSuitDes: str


class WeaponEffect(BaseModel):
    title: Annotated[str, BeforeValidator(lambda x: x.replace(':', '').replace('*', '') if x and str(x).endswith(':') else x)]
    description: str


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
    value: float = Field(0, validation_alias=AliasChoices('PropValue', 'value'))
    isTag: bool = Field(False, validation_alias=AliasChoices('IsTag', 'isTag'))
    modifier: str = Field('', validation_alias=AliasChoices('modifier', 'ModifierOp'))


class UpgradeMaterial(BaseModel):
    id: str
    need: int | None