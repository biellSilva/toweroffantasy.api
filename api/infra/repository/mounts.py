
import json

from pathlib import Path
from typing import Any

from api.core.exceptions import *
from api.enums import LANGS, LANGS_CN, VERSIONS
from api.utils import sort_mounts

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Mount, EntityBase


class MountsRepo(ModelRepository[EntityBase, Mount]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Mount, 
                         class_base=MountsRepo,
                         repo_name='mount')
    
    
    async def get_all(self, lang: LANGS | LANGS_CN | str, version: VERSIONS) -> list[Mount]:
        if version in self.cache:
            if lang in self.cache[version]:
                return list(self.cache[version][lang].values())

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

        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        for key_id, value_dict in DATA.items():
            
            if 'only' in value_dict['version'].lower():
                continue

            if value_dict.get('id', None):
                self.cache[version][lang].update({key_id.lower(): self.model(**value_dict)})
            else:
                self.cache[version][lang].update({key_id.lower(): self.model(**value_dict, id=key_id)})
        
        self.cache[version][lang] = {i.id: i for i in list(sorted(list(self.cache[version][lang].values()), key=sort_mounts))}

        return list(self.cache[version][lang].values())