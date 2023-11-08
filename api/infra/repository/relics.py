

from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Relic, EntityBase


class RelicRepo(ModelRepository[EntityBase, Relic]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Relic, 
                         class_base=RelicRepo,
                         repo_name='relics')
    
    async def get_all(self, lang: str) -> list[Relic]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/database/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for relic_id, relic_dict in DATA.items():
                self.cache[lang].update({relic_id.lower(): Relic(**relic_dict)})

            return list(self.cache[lang].values())