import json
from pathlib import Path

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.matrices import Matrix
from src.domain.models.meta import MetaData
from src.enums import LANGS_GLOBAL_ENUM
from src.infra.models.matrices import RawMatrix
from src.infra.repository.helpers.matrices import ignore_matrix, matrix_set_rework


class MatricesGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, Matrix]] = {}

    __LINK_DATA: dict[str, dict[str, str]] = json.loads(
        Path("src/infra/database/imitation_links.json").read_bytes()
    )
    __META_DATA: dict[str, MetaData] = {
        k: MetaData(**v)
        for k, v in json.loads(
            Path("src/infra/database/global/meta.json").read_bytes()
        ).items()
    }

    async def find_by_id(
        self,
        id: str,
        lang: LANGS_GLOBAL_ENUM,
    ) -> Matrix | None:

        if lang_cache := self.__cache.get(lang):
            if matrix := lang_cache.get(id):
                return matrix
            return None

        await self.load_data(lang=lang)
        return await self.find_by_id(id=id, lang=lang)

    async def get_all(self, lang: LANGS_GLOBAL_ENUM) -> list[Matrix]:

        if lang_cache := self.__cache.get(lang):
            return list(lang_cache.values())

        await self.load_data(lang=lang)
        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_GLOBAL_ENUM) -> None:

        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "matrices.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

        DATA: dict[str, RawMatrix] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():
            if ignore_matrix(value_dict):
                continue

            value_dict = matrix_set_rework(dict_=value_dict)

            for i in self.__LINK_DATA:
                if isinstance(self.__LINK_DATA.get(i, {}).get("matrice", None), str):
                    if self.__LINK_DATA[i]["matrice"].lower() == key_id.lower():
                        value_dict["simulacrumId"] = i

            value_dict["meta"] = {}
            value_dict["meta"]["recommendedWeapons"] = [
                k
                for k, v in self.__META_DATA.items()
                for matrix in v.recommendedMatrices
                if key_id.lower() == matrix.id.lower()
            ]

            self.__cache[lang].update(
                {key_id.lower(): Matrix(**value_dict)}  # type: ignore
            )
