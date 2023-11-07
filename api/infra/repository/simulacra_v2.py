
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Simulacra, EntityBase


class SimulacraRepo(ModelRepository[EntityBase, Simulacra]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Simulacra, 
                         class_base=SimulacraRepo,
                         repo_name='simulacra')
    
    async def get_all(self, lang: str) -> list[Simulacra]:
        if self.__load_all_data__:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/database/{lang}/imitations.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass
            else:
                self.cache.update({lang: {}})

            for imit_id, imit_dict in DATA.items():
                if 'L1' not in imit_id:
                    va: list[dict[str, str]] = imit_dict.pop('va')
                    imit_dict['va'] = {key.lower(): value for i in va for key, value in i.items()}
                    self.cache[lang].update({imit_id.lower(): Simulacra(**imit_dict)})

            self.__load_all_data__ = True
            return list(self.cache[lang].values())