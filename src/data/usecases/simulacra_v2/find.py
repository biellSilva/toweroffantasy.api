from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.simulacra_v2.find import (
    FindSimulacraV2Params,
    IFindSimulacraV2UseCase,
)
from src.infra.repository.simulacra_v2.global_ import SimulacraV2GlobalRepository


class FindSimulacraV2UseCase(IFindSimulacraV2UseCase):
    def __init__(self, repository: SimulacraV2GlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindSimulacraV2Params) -> SimulacraV2:
        if params.version == "global":
            if data := await self.repository.find_by_id(
                **params.model_dump(exclude={"version"})
            ):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr