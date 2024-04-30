import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import DataIncompleteErr, LangNotFoundErr
from src.domain.models.simulacra import Simulacra
from src.enums import LANGS_CHINA_ENUM, VERSIONS_ENUM
from src.infra.models.simulacra import RawSimulacra
from src.infra.repository.helpers.simulacra import sort_simulacra
from src.infra.repository.helpers.unlockables import add_unlockables


class SimulacraChinaRepository:
    __cache: dict[LANGS_CHINA_ENUM, dict[str, Simulacra]] = {}

    def __init__(self) -> None:
        super().__init__()

    async def find_by_id(
        self, id: str, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> Simulacra | None:

        if cached_lang := self.__cache.get(lang):
            if simulacra := cached_lang.get(id):
                return simulacra
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> list[Simulacra]:
        if cached_lang := self.__cache.get(lang):
            return list(cached_lang.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_CHINA_ENUM) -> None:

        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/china", lang, "imitations.json")
        WEAPONS_PATH = Path("./src/infra/database/china", lang, "weapons.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        if not WEAPONS_PATH.exists():
            raise DataIncompleteErr

        DATA: dict[str, RawSimulacra] = json.loads(DATA_PATH.read_bytes())
        WEAPONS: dict[str, dict[str, Any]] = json.loads(WEAPONS_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            value_dict = add_unlockables(
                dict_=value_dict, version=VERSIONS_ENUM("china"), lang=lang
            )

            if weapon_data := WEAPONS.get(value_dict["weaponId"]):
                value_dict["fashion"] = [
                    fashion["outfit"]
                    for fashion in weapon_data.get("fashion", [])
                    if "outfit" in fashion
                ]

            self.__cache[lang].update(
                {key_id.lower(): Simulacra(**value_dict)}  # type: ignore
            )

        self.__cache[lang] = sort_simulacra(self.__cache[lang])
