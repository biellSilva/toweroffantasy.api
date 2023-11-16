
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Food, EntityBase
from api.infra.repository.item import ItemRepo


class FoodRepo(ModelRepository[EntityBase, Food]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Food, 
                         class_base=FoodRepo,
                         repo_name='food')
        self.item_repo = ItemRepo()
    
    async def get_all(self, lang: str) -> list[Food]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/infra/database/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for food_id, food_dict in DATA.items():
                if 'ingredients' in food_dict:
                    for i in food_dict['ingredients']:

                        if isinstance(i['min'], str):
                            i['min'] = int(i['min'])

                        if isinstance(i['max'], str):
                            i['max'] = int(i['max'])
                        
                        if item := await self.item_repo.get(EntityBase(id=i['matID'].lower()), lang):
                            i['item'] = item.model_dump()

                self.cache[lang].update({food_id.lower(): Food(**food_dict, id=food_id)})

            return list(self.cache[lang].values())
    