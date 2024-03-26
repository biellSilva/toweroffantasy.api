import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.matrices import Matrix
from src.enums import LANGS_CHINA_ENUM
from src.infra.models.matrices import RawMatrix
from src.infra.repository.helpers.matrices import matrix_set_rework, sort_matrices


class MatricesChinaRepository:
    __cache: dict[LANGS_CHINA_ENUM, dict[str, Matrix]] = {}

    __LINK_DATA: dict[str, dict[str, str]] = json.loads(
        Path("src/infra/database/imitation_links.json").read_bytes()
    )

    async def find_by_id(
        self, id: str, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> Matrix | None:

        if lang_cache := self.__cache.get(lang):
            if matrix := lang_cache.get(id):
                return matrix
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(
        self, lang: LANGS_CHINA_ENUM, *args: Any, **kwargs: Any
    ) -> list[Matrix]:

        if lang_cache := self.__cache.get(lang):
            return list(lang_cache.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_CHINA_ENUM) -> None:

        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/china", lang, "matrices.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, RawMatrix] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            value_dict = matrix_set_rework(dict_=value_dict)

            for i in self.__LINK_DATA:
                if isinstance(self.__LINK_DATA.get(i, {}).get("matrice", None), str):
                    if self.__LINK_DATA[i]["matrice"].lower() == key_id.lower():
                        value_dict["simulacrumId"] = i

            self.__cache[lang].update(
                {key_id.lower(): Matrix(**value_dict)}  # type: ignore
            )

        self.__cache[lang] = sort_matrices(self.__cache[lang])
