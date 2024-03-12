from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field

from src.domain.models.weapons import Weapon
from src.domain.usecases.base import IUsecase


class GetAllWeaponsParams(BaseModel):
    version: str = Field("global", description="Game version")
    lang: str = Field("en", description="Game language")
    filter: dict[str, Any] = Field(
        {},
        description="Filter to apply to the models",
        examples=[{"awakening.need": 4000}, {"limited": True}],
    )


class IGetAllWeaponsUseCase(IUsecase[GetAllWeaponsParams, Weapon], ABC):
    @abstractmethod
    async def execute(self, params: GetAllWeaponsParams) -> list[Weapon]: ...
