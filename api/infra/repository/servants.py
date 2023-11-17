
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import SmartServant, EntityBase


class ServantsRepo(ModelRepository[EntityBase, SmartServant]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=SmartServant, 
                         class_base=ServantsRepo,
                         repo_name='pet')
    
    async def get_all(self, lang: str) -> list[SmartServant]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/infra/database/global/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for servant_id, servant_dict in DATA.items():
                servant_dict['id'] = servant_id.lower()
                servant_dict['upgradeItems'] = [{'id': key.lower(), 'xpGain': value} for key, value in servant_dict['PetUpgradeItemMap'].items()]
                self.cache[lang].update({servant_id.lower(): SmartServant(**servant_dict)})

            self.__load_all_data__ = True
            return list(self.cache[lang].values())
    