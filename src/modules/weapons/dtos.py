from typing import Annotated

from fastapi import Path
from pydantic import Field

from src.common.dtos import BaseSearchAllDto, BaseSearchDto


class GetWeapon(BaseSearchDto):
    weapon_id: Annotated[str, Path(description="Weapon id")]


class GetWeapons(BaseSearchAllDto):
    name: str | None = Field(None, description="Name should be part of")
    is_fate: bool | None = Field(None, description="Is fate weapon")
    is_limited: bool | None = Field(None, description="Is limited weapon")
    is_warehouse: bool | None = Field(
        None,
        description="Is warehouse (player's inventory) weapon",
    )
    shatter_value: int | None = Field(None, description="Shatter value", ge=1)
    charge_value: int | None = Field(None, description="Charge value", ge=1)
    shatter_tier: str | None = Field(None, description="Shatter tier (A, B, C, ...)")
    charge_tier: str | None = Field(None, description="Charge tier (A, B, C, ...)")
    include_ids: list[str] | None = Field(None, description="ID should be one of")
    exclude_ids: list[str] | None = Field(None, description="ID should not be one of")
    include_elements: list[str] | None = Field(
        None,
        description="Element ID should include one of",
    )
    exclude_elements: list[str] | None = Field(
        None,
        description="Element ID should exclude one of",
    )
    include_categories: list[str] | None = Field(
        None,
        description="Category ID should include one of",
    )
    exclude_categories: list[str] | None = Field(
        None,
        description="Category ID should exclude one of",
    )
    include_rarities: list[str] | None = Field(
        None,
        description="Rarity should include one of",
    )
    exclude_rarities: list[str] | None = Field(
        None,
        description="Rarity should exclude one of",
    )
    include_qualities: list[str] | None = Field(
        None,
        description="Quality should include one of",
    )
    exclude_qualities: list[str] | None = Field(
        None,
        description="Quality should exclude one of",
    )
