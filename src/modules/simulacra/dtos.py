from typing import Annotated

from fastapi import Path, Query

from src.modules.base.dtos import BaseSearchAllDto, BaseSearchDto


class GetSimulacrum(BaseSearchDto):
    simulacrum_id: Annotated[str, Path(description="Simulacrum id")]


class GetSimulacra(BaseSearchAllDto):
    name: Annotated[str | None, Query(description="Name should be part of")] = None
    is_limited: Annotated[
        bool | None,
        Query(description="Is limited weapon (Red Nucleous)"),
    ] = None
    no_weapon: Annotated[bool | None, Query(description="No weapon (Polymorph)")] = None
