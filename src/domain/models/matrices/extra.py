from typing import Annotated

import strawberry
from pydantic import AliasChoices, BaseModel, BeforeValidator, Field

from src.utils import bold_numbers


class MatrixAsset(BaseModel):
    icon: str | None = Field(validation_alias=AliasChoices("itemIcon", "icon"))
    itemLarge: str | None = Field(
        None, validation_alias=AliasChoices("ItemIconLarge", "iconLarge")
    )
    characterArtwork: str | None = None


class MatrixSet(BaseModel):
    need: int
    description: Annotated[str, BeforeValidator(bold_numbers)]


class MatrixMeta(BaseModel):
    recommendedWeapons: list[str] = []


@strawberry.experimental.pydantic.type(model=MatrixAsset, all_fields=True)
class MatrixAssetType:
    pass


@strawberry.experimental.pydantic.type(model=MatrixSet, all_fields=True)
class MatrixSetType:
    pass


@strawberry.experimental.pydantic.type(model=MatrixMeta, all_fields=True)
class MatrixMetaType:
    pass
