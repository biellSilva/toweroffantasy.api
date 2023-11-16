
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Matrix, EntityBase

from api.utils import matrice_set_rework


class MatricesRepo(ModelRepository[EntityBase, Matrix]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Matrix, 
                         class_base=MatricesRepo,
                         repo_name='matrices')
    
    async def get_all(self, lang: str) -> list[Matrix]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/database/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for matrice_id, matrice_dict in DATA.items():
                matrice_id = matrice_id.removesuffix('_1').lower()
                matrice_dict['id'] = matrice_id

                matrice_dict['sets'] = matrice_set_rework(rarity=matrice_dict.get('rarity', ''),
                                                         sets=matrice_dict.pop('set'))

                self.cache[lang].update({matrice_id: Matrix(**matrice_dict)})

            self.__load_all_data__ = True
            return list(self.cache[lang].values())
    
    async def get_by_name(self, name: str, lang: str):
        for i in await self.get_all(lang):
            if i.name == name:
                return i