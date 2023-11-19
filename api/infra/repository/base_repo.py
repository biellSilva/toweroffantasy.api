
import json

from typing import TypeVar, Type, Any
from pathlib import Path

from api.infra.interface import IRepository
from api.infra.entitys import EntityBase

from api.enums import LANGS, LANGS_CN, VERSIONS

from api.core.exceptions import ItemNotFound, LanguageNotFound, VersionNotFound, FileNotFound


B = TypeVar('B', bound=EntityBase)
T = TypeVar('T', bound=EntityBase)


class ModelRepository(IRepository[B, T]):
    def __init__(self, model_base: Type[B], model: Type[T], class_base: Type[IRepository[B, T]], repo_name: str) -> None:
        self.model_base = model_base
        self.model = model
        self.class_base = class_base
        self.repo_name = repo_name
        
    async def get(self, model: B, lang: LANGS | LANGS_CN, version: VERSIONS) -> T:
        if version in self.class_base.cache:
            if lang in self.class_base.cache[version]:
                if model.id in self.class_base.cache[version][lang]:
                    return self.class_base.cache[version][lang][model.id]
                else:
                    raise ItemNotFound(model.id, lang, version)

        await self.get_all(lang=lang, version=version)
        return await self.get(model, lang, version)
    

    async def get_all(self, lang: LANGS | LANGS_CN, version: VERSIONS) -> list[T]:
        if version in self.class_base.cache:
            if lang in self.class_base.cache[version]:
                return list(self.class_base.cache[version][lang].values())

        VERSION_PATH = Path(f'api/infra/database/{version}')
        if not VERSION_PATH.exists():
            raise VersionNotFound(version)
        
        LANG_PATH = Path(VERSION_PATH, lang)
        if not LANG_PATH.exists():
            raise LanguageNotFound(lang, version)

        FILEPATH = Path(LANG_PATH, f'{self.repo_name}.json')
        if not FILEPATH.exists():
            raise FileNotFound(self.repo_name, lang, version)

        DATA: dict[str, dict[str, Any]] = json.loads(FILEPATH.read_bytes())

        if version not in self.class_base.cache:
            self.class_base.cache.update({version: {}})

        if lang not in self.class_base.cache[version]:
            self.class_base.cache[version].update({lang: {}})

        for key_id, value_dict in DATA.items():
            if value_dict.get('id', None):
                self.class_base.cache[version][lang].update({key_id.lower(): self.model(**value_dict)})
            else:
                self.class_base.cache[version][lang].update({key_id.lower(): self.model(**value_dict, id=key_id)})

        return list(self.class_base.cache[version][lang].values())