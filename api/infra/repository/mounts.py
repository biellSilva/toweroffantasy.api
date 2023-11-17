
from pathlib import Path
from json import loads
from typing import Any

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
    
    async def get_all(self, lang: str) -> list[Mount]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/infra/database/global/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for mount_id, mount_dict in DATA.items():
                self.cache[lang].update({mount_id: Mount(**mount_dict)})

            self.__load_all_data__ = True
            return list(self.cache[lang].values())
    