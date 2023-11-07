
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Weapon, EntityBase


class WeaponRepo(ModelRepository[EntityBase, Weapon]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Weapon, 
                         class_base=WeaponRepo,
                         repo_name='weapon')
    
    async def get_all(self, lang: str) -> list[Weapon]:
        if self.__load_all_data__:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/database/{lang}/weapons.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for Weapon_id, Weapon_dict in DATA.items():
                
                set: list[dict[str, str]] = Weapon_dict.pop('set')
                Weapon_dict['set'] = {key.lower(): value for i in set for key, value in i.items()}
                self.cache[lang].update({Weapon_id.lower(): Weapon(**Weapon_dict)})

            self.__load_all_data__ = True
            return list(self.cache[lang].values())