import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import DataIncompleteErr, LangNotFoundErr
from src.domain.models.simulacra_v2 import SimulacraV2
from src.enums import LANGS_CHINA_ENUM, VERSIONS_ENUM
from src.infra.models.simulacra import RawSimulacra
from src.infra.repository.helpers.simulacra_v2 import sort_simulacra
from src.infra.repository.helpers.unlockables import add_unlockables
from src.infra.repository.matrices.china import MatricesChinaRepository
from src.infra.repository.weapons.china import WeaponsChinaRepository


class SimulacraV2ChinaRepository:
    __cache: dict[LANGS_CHINA_ENUM, dict[str, SimulacraV2]] = {}

    def __init__(self) -> None:
        super().__init__()

        self.__WEAPONS_REPO = WeaponsChinaRepository()
        self.__MATRICES_REPO = MatricesChinaRepository()

    async def find_by_id(
        self, id: str, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> SimulacraV2 | None:

        if cached_lang := self.__cache.get(lang):
            if simulacra := cached_lang.get(id):
                return simulacra
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> list[SimulacraV2]:
        if cached_lang := self.__cache.get(lang):
            return list(cached_lang.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_CHINA_ENUM) -> None:

        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/china", lang, "imitations.json")
        WEAPON_PATH = Path("./src/infra/database/china", lang, "weapons.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        if not WEAPON_PATH.exists():
            raise DataIncompleteErr

        DATA: dict[str, RawSimulacra] = json.loads(DATA_PATH.read_bytes())
        WEAPON_DATA: dict[str, dict[str, Any]] = json.loads(WEAPON_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            value_dict = add_unlockables(
                dict_=value_dict, version=VERSIONS_ENUM("china"), lang=lang
            )

            if weapon_id := value_dict.get("weaponId"):
                value_dict["weapon"] = await self.__WEAPONS_REPO.find_by_id(
                    id=weapon_id.lower(), lang=lang
                )

            if matrix_id := value_dict.get("matrixId"):
                value_dict["matrix"] = await self.__MATRICES_REPO.find_by_id(
                    id=matrix_id.lower(), lang=lang
                )

            if weapon_data := WEAPON_DATA.get(value_dict["weaponId"]):
                value_dict["fashion"] = [
                    fashion["outfit"] for fashion in weapon_data.get("fashion", [])
                ]

            self.__cache[lang].update(
                {key_id.lower(): SimulacraV2(**value_dict)}  # type: ignore
            )
        self.__cache[lang] = sort_simulacra(self.__cache[lang])