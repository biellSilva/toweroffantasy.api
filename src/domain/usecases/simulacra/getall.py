from abc import ABC, abstractmethod

from src.domain.models.simulacra import Simulacra
from src.domain.usecases.base import GetAllParams, IUsecase


# class GetallSimulacraParams(BaseModel):
#     version: str = Field("global", description="Game version")
#     lang: str = Field("en", description="Game language")
#     filter: dict[str, Any] = Field(
#         {},
#         description="Filter to apply to the models",
#         examples=[{"awakening.need": 4000}, {"limited": True}],
#     )


class IGetallSimulacraUseCase(IUsecase[GetAllParams, Simulacra], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Simulacra]: ...
