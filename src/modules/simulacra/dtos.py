from typing import Annotated

from fastapi import Path
from pydantic import Field

from src.modules.base.dtos import BaseSearchAllDto, BaseSearchDto


class GetSimulacrum(BaseSearchDto):
    simulacrum_id: Annotated[str, Path(description="Simulacrum id")]


class GetSimulacra(BaseSearchAllDto):
    name: str | None = Field(None, description="Name should be part of")
    is_limited: bool | None = Field(
        None,
        description="Is limited weapon (Red Nucleous)",
    )

    no_weapon: bool | None = Field(None, description="No weapon (Polymorph)")
    include_ids: list[str] | None = Field(None, description="Id should be one of")
    exclude_ids: list[str] | None = Field(None, description="Id should not be one of")
    include_sex: list[str] | None = Field(None, description="Sex should include one of")
    exclude_sex: list[str] | None = Field(None, description="Sex should exclude one of")
    include_rarities: list[str] | None = Field(
        None,
        description="Rarity should include one of",
    )
    exclude_rarities: list[str] | None = Field(
        None,
        description="Rarity should exclude one of",
    )
