
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Item, EntityBase


class ItemRepo(ModelRepository[EntityBase, Item]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Item, 
                         class_base=ItemRepo,
                         repo_name='items')
    
    async def get_all(self, lang: str) -> list[Item]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/infra/database/global/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for item_id, item_dict in DATA.items():
                self.cache[lang].update({item_id.lower(): Item(**item_dict)})

            return list(self.cache[lang].values())
    