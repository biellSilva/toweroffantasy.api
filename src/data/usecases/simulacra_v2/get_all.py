from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.simulacra_v2.get_all import (
    GetAllSimulacraV2Params,
    IGetAllSimulacraV2UseCase,
)
from src.infra.repository.simulacra_v2.global_ import SimulacraV2GlobalRepository


class GetAllSimulacraV2UseCase(IGetAllSimulacraV2UseCase):
    def __init__(self, repository: SimulacraV2GlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllSimulacraV2Params) -> list[SimulacraV2]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
