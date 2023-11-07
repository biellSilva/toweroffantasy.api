
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
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/database/{lang}/weapons.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for weapon_id, weapon_dict in DATA.items():
                stars = weapon_dict.get('stars', [])
                weaponEffects: list[dict[str, str]] = []
                if stars: 
                    if 'description' in stars[0]:
                        if description := stars[0]['description']:
                            if '*:' in description:
                                weaponEffect = description.split('\r', 1)

                                for i in weaponEffect:
                                    key, value_ = i.split('*:', 1)
                                    key = key.replace('*', '').replace('\n', '').replace('\r', '')
                                    value_ = value_.replace('\n', '').replace('\r', '').replace(' ', '', 1)
                                    weaponEffects.append({'title': key, 'description': value_})
                            else:
                                if weapon_dict['name'].lower() == 'shadoweave':
                                    weaponEffects = [{'title': 'Altered Damage', 'description': description.replace('\n', ' ').replace('\r', '')}]
                                else:
                                    weaponEffects = [{'title': 'Unknown', 'description': description.replace('\n', ' ').replace('\r', '')}]

                    weapon_dict['stars'].pop(0)
                    
                weapon_dict.update({'weaponEffects': weaponEffects})

                self.cache[lang].update({weapon_id.lower(): Weapon(**weapon_dict)})

            return list(self.cache[lang].values())