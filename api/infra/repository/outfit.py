
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Outfit, EntityBase


class OutfitRepo(ModelRepository[EntityBase, Outfit]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Outfit, 
                         class_base=OutfitRepo,
                         repo_name='outfits')
    
    async def get_all(self, lang: str) -> list[Outfit]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/infra/database/global/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for outfit_id, outfit_data in DATA.items():
                self.cache[lang].update({outfit_id.lower(): Outfit(**outfit_data)})

            return list(self.cache[lang].values())
    