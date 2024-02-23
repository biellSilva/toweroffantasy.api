from typing import Annotated
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
