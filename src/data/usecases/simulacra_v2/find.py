from src.domain.errors.http import NotFoundErr, VersionNotFoundErr
from src.domain.models.simulacra_v2 import SimulacraV2
from src.domain.usecases.base import FindParams
from src.domain.usecases.simulacra_v2.find import IFindSimulacraV2UseCase
from src.infra.repository.simulacra_v2.china import SimulacraV2ChinaRepository
from src.infra.repository.simulacra_v2.global_ import SimulacraV2GlobalRepository


class FindSimulacraV2UseCase(IFindSimulacraV2UseCase):
    def __init__(
        self,
        repository: SimulacraV2GlobalRepository,
        china_repository: SimulacraV2ChinaRepository,
    ) -> None:
        self.repository = repository
        self.china_repository = china_repository

    async def execute(self, params: FindParams) -> SimulacraV2:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            if data := await self.china_repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        else:
            raise VersionNotFoundErr
