
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Simulacra, EntityBase

from api.utils import replace_rating
from api.enums import LANGS


class SimulacraRepo(ModelRepository[EntityBase, Simulacra]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Simulacra, 
                         class_base=SimulacraRepo,
                         repo_name='imitations')
    
    async def get_all(self, lang: str) -> list[Simulacra]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/database/{lang}/{self.repo_name}.json')
            BANNERS_PATH = Path(f'api/database/banners_global.json')

            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())
            BANNERS_DATA: list[dict[str, str | int | bool]] = loads(BANNERS_PATH.read_bytes())

            if lang in self.cache:
                pass
            else:
                self.cache.update({lang: {}})

            for imit_id, imit_dict in DATA.items():
                if 'L1' not in imit_id:
                    
                    imit_dict['banners'] = [banner for banner in BANNERS_DATA if banner['imitation_id'] == imit_id]
                    
                    imit_dict['assets']['icon'] = imit_dict['avatarID']

                    va: list[dict[str, str]] = imit_dict.pop('va')
                    imit_dict['va'] = {key.lower(): value for i in va for key, value in i.items()}

                    traits: dict[str, dict[str, str] | str] = imit_dict.get('trait', {})
                    imit_dict['trait'] = [i for i in traits.values() if isinstance(i, dict)]

                    imit_dict['rating'] = replace_rating(imit_dict['rating'], LANGS(lang))

                    self.cache[lang].update({imit_id.lower(): Simulacra(**imit_dict)})

            self.__load_all_data__ = True
            return list(self.cache[lang].values())