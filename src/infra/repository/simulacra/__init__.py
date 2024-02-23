from src.data.protocols.db.simulacra.find import FindSimulacraRepository
from src.domain.models.simulacra import Simulacra
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM


class SimulacraRepository(FindSimulacraRepository):
    cache: dict[
        VERSIONS_ENUM,
        dict[LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM, dict[str, Simulacra]],
    ] = {}

    def __init__(self) -> None:
        super().__init__()

    async def find_by_id(
        self,
        id: str,
        version: VERSIONS_ENUM,
        lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
    ) -> Simulacra | None:

        if version in self.cache:
            if lang in self.cache[version]:
                if simulacra := self.cache[version][lang].get(id):
                    return simulacra
