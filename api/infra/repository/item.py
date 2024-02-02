import json
from pathlib import Path
from typing import Any

from api.core.exceptions import FileNotFound, LanguageNotFound, VersionNotFound
from api.enums import LANGS, LANGS_CN, VERSIONS
from api.infra.entitys import EntityBase, Item
from api.infra.repository.base_repo import ModelRepository


class ItemRepo(ModelRepository[EntityBase, Item]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(
            model_base=EntityBase, model=Item, class_base=ItemRepo, repo_name="items"
        )

    async def get_all(
        self, lang: LANGS | LANGS_CN | str, version: VERSIONS
    ) -> list[Item]:
        if version in self.class_base.cache:
            if lang in self.class_base.cache[version]:
                return list(self.class_base.cache[version][lang].values())

        VERSION_PATH = Path(f"api/infra/database/{version}")
        if not VERSION_PATH.exists():
            raise VersionNotFound(version)

        LANG_PATH = Path(VERSION_PATH, lang)
        if not LANG_PATH.exists():
            raise LanguageNotFound(lang, version)

        FILEPATH = Path(LANG_PATH, f"{self.repo_name}.json")
        if not FILEPATH.exists():
            raise FileNotFound(self.repo_name, lang, version)

        CURRENCY2_DATA = Path(LANG_PATH, f"currency2.json")
        if not CURRENCY2_DATA.exists():
            raise FileNotFound(self.repo_name, lang, version)

        DATA: dict[str, dict[str, Any]] = json.loads(FILEPATH.read_bytes())
        DATA_2: dict[str, dict[str, Any]] = json.loads(CURRENCY2_DATA.read_bytes())

        DATA.update(DATA_2)

        if version not in self.class_base.cache:
            self.class_base.cache.update({version: {}})

        if lang not in self.class_base.cache[version]:
            self.class_base.cache[version].update({lang: {}})

        for key_id, value_dict in DATA.items():
            if value_dict.get("id", None):
                self.class_base.cache[version][lang].update(
                    {key_id.lower(): self.model(**value_dict)}
                )
            else:
                self.class_base.cache[version][lang].update(
                    {key_id.lower(): self.model(**value_dict, id=key_id)}
                )

        return list(self.class_base.cache[version][lang].values())
