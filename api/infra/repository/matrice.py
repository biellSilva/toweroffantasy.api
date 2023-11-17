
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
    
    def __sort_matrice(self, item: Matrix):
        if item.rarity == 'SSR':
            return (1, -int(item.id.rsplit('ssr', 1)[1]))
        elif item.rarity == 'SR':
            return (2, -int(item.id.rsplit('sr', 1)[1]))
        elif item.rarity == 'R':
            return (3, -int(item.id.rsplit('r', 1)[1]))
        else:
            return (4, -int(item.id.rsplit('n', 1)[1]))

    
    async def get_all(self, lang: str) -> list[Matrix]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/infra/database/global/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for matrice_id, matrice_dict in DATA.items():
                if matrice_id in ('matrix_SSR12_1', 'matrix_SSR13_1'):
                    continue
                
                matrice_id = matrice_id.removesuffix('_1').lower()
                matrice_dict['id'] = matrice_id

                matrice_dict['sets'] = matrice_set_rework(rarity=matrice_dict.get('rarity', ''),
                                                         sets=matrice_dict.pop('set'))

                self.cache[lang].update({matrice_id: Matrix(**matrice_dict)})

            self.cache[lang] = {i.id: i for i in list(sorted(list(self.cache[lang].values()), key=self.__sort_matrice))}
            
            return list(self.cache[lang].values())
    
    async def get_by_name(self, name: str, lang: str):
        for i in await self.get_all(lang):
            if i.name == name:
                return i