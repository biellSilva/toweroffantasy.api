from typing import Annotated

from fastapi import Path

from src.modules.base.dtos import BaseSearchDto


class GetSimulacrum(BaseSearchDto):
    simulacrum_id: Annotated[str, Path(description="Simulacrum id")]

