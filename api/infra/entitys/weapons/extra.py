
from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

from api.utils import bold_numbers, replace_icon


class Skill(BaseModel):
    id: str
    icon: Annotated[str, BeforeValidator(replace_icon)]
    name: str
    description: Annotated[str, BeforeValidator(bold_numbers)]

class Skills(BaseModel):
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]

class Stats(BaseModel):
    shatter: int | float
    charge: int | float

class Advancements(BaseModel):
    description: Annotated[str, BeforeValidator(bold_numbers)] | None = None
    stats: Stats
    need: str

class WeaponEffect(BaseModel):
    title: str
    description: str

class ShatterOrCharge(BaseModel):
    value: float
    tier: str

class Assets(BaseModel):
    icon: Annotated[str, BeforeValidator(replace_icon)] | None = None
    weaponMatrixIcon: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='WeaponIconForMatrix', serialization_alias='weaponMatrixIcon')
    bannerIcon: Annotated[str, BeforeValidator(replace_icon)] | None = Field(default=None, alias='SoloLeagueBanPickBanner', serialization_alias='bannerIcon')

class RecoMatrix(BaseModel):
    id: str
    pieces: int


class Meta(BaseModel):
    recommendedPairings: list[str] = []
    recommendedMatrices: list[RecoMatrix] = []
    rating: list[int] = []
    analyticVideoId: str | None = None