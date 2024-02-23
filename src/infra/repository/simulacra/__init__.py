import json
from pathlib import Path
from typing import NoReturn

from src.data.protocols.db.simulacra.find import FindSimulacraRepository
from src.domain.errors.http import DataNotFoundErr
from src.domain.models.simulacra import Simulacra
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM
from src.infra.models.simulacra import RawSimulacra
from src.infra.repository.simulacra._helpers import ignore_simulacra, sort_simulacra
from src.infra.repository.simulacra._helpers.unlockables import add_unlockables


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

        if cached_version := self.cache.get(version):
            if cached_lang := cached_version.get(lang):
                if simulacra := cached_lang.get(id):
                    return simulacra
                return None

        await self.load_data(version=version, lang=lang)

    async def get_all(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> list[Simulacra]:
        if cached_version := self.cache.get(version):
            if cached_lang := cached_version.get(lang):
                return list(cached_lang.values())

        await self.load_data(version=version, lang=lang)

    async def load_data(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> NoReturn:

        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        DATA_PATH = Path("./src/infra/database", version, lang, "imitations.json")

        if not DATA_PATH.exists():
            raise DataNotFoundErr

        DATA: dict[str, RawSimulacra] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():
            if ignore_simulacra(value_dict):
                continue

            value_dict = add_unlockables(dict_=value_dict, version=version, lang=lang)

            self.cache[version][lang].update({key_id.lower(): Simulacra(**value_dict)})  # type: ignore

        self.cache[version][lang] = sort_simulacra(self.cache[version][lang])
