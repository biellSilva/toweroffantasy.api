
import json

from pathlib import Path
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Matrix, EntityBase

from api.core.exceptions import FileNotFound, VersionNotFound, LanguageNotFound

from api.enums import LANGS, LANGS_CN, VERSIONS
from api.utils import matrice_set_rework, sort_matrices
from api.config import GB_BANNERS


class MatricesRepo(ModelRepository[EntityBase, Matrix]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Matrix, 
                         class_base=MatricesRepo,
                         repo_name='matrices')
    
    async def get_all(self, lang: LANGS | LANGS_CN, version: VERSIONS) -> list[Matrix]:
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

        for matrice_id, matrice_dict in DATA.items():
            if version == 'global' and matrice_id in ('matrix_SSR12_1', 'matrix_SSR13_1'):
                continue
            
            matrice_id = matrice_id.removesuffix('_1').lower()
            matrice_dict['id'] = matrice_id

            matrice_dict['sets'] = matrice_set_rework(rarity=matrice_dict.get('rarity', ''),
                                                    sets=matrice_dict.pop('set'))
            
            if version == 'global':
                matrice_dict['banners'] = [banner for banner in GB_BANNERS if banner.matrix_id and banner.matrix_id == matrice_id.lower()]

            self.cache[version][lang].update({matrice_id: Matrix(**matrice_dict)})

        self.cache[version][lang] = {i.id: i for i in list(sorted(list(self.cache[version][lang].values()), key=sort_matrices))}
        
        return list(self.cache[version][lang].values())
