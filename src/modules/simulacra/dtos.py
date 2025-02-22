from typing import Annotated

from fastapi import Path, Query

from src.modules.base.dtos import BaseSearchDto


class GetSimulacrum(BaseSearchDto):
    simulacrum_id: Annotated[str, Path(description="Simulacrum id")]


class GetSimulacra(BaseSearchDto):
    page: Annotated[int, Query(description="Page number", ge=1)] = 1
    limit: Annotated[int, Query(description="Items limit", ge=1, le=100)] = 25

    is_limited: Annotated[bool | None, Query(description="Is limited")] = None
    no_weapon: Annotated[bool | None, Query(description="No weapon")] = None
