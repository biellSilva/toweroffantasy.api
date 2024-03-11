from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.simulacra import Simulacra
from src.domain.usecases.simulacra.find import (
    FindSimulacraParams,
    IFindSimulacraUseCase,
)
from src.infra.repository.simulacra.global_ import SimulacraGlobalRepository


class FindSimulacraUseCase(IFindSimulacraUseCase):
    def __init__(self, repository: SimulacraGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindSimulacraParams) -> Simulacra:
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
