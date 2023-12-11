
from pydantic import BaseModel, BeforeValidator, model_validator
from typing import Annotated, Any

from api.utils import replace_icon, classify_rework, bold_numbers


class ListKeys(BaseModel):
    Time: float
    Value: float


class Assets(BaseModel):
    icon: str | None
    # itemLargeIcon: str | None
    # WeaponUPIcon: str | None
    weaponIconForMatrix: str | None

    @model_validator(mode='before')
    def _replace_assets(cls, values: Any):

        def _replace_string__(value: Any) -> Any:
            if isinstance(value, dict):
                _: dict[str, Any] = {}

                for k, v in values.items():
                    if isinstance(v, str):
                        _.update({k: v.replace('/Game/Resources', '/assets')})

                    else:
                        _.update({k: v})

                return _
            
            return value

        return _replace_string__(values)


class Skill(BaseModel):
    name: str | None
    description: Annotated[str, BeforeValidator(bold_numbers)] | None
    values: list[list[float | int]] = []
    icon: str | None
    tags: list[str] = []
    operations: list[str] = []
    id: str


    @model_validator(mode='before')
    def _replace_assets(cls, values: Any):

        def _replace_string__(value: Any) -> Any:
            if isinstance(value, dict):
                _: dict[str, Any] = {}

                for k, v in values.items():
                    if isinstance(v, str):
                        _.update({k: v.replace('/Game/Resources', '/assets')})

                    else:
                        _.update({k: v})

                return _
            
            return value

        return _replace_string__(values)


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
    title: str
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


class UpgradeMaterial(BaseModel):
    id: str
    need: int | None