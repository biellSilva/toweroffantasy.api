
from pathlib import Path
from json import loads
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Achievement, EntityBase


class AchievementRepo(ModelRepository[EntityBase, Achievement]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Achievement, 
                         class_base=AchievementRepo,
                         repo_name='achievements')
    
    async def get_all(self, lang: str) -> list[Achievement]:
        if lang in self.cache:
            return list(self.cache[lang].values())
        
        else:
            PATH_IMIT = Path(f'api/infra/database/{lang}/{self.repo_name}.json')
            DATA: dict[str, dict[str, Any]] = loads(PATH_IMIT.read_bytes())

            if lang in self.cache:
                pass

            else:
                self.cache.update({lang: {}})

            for achievement_id, achievement_dict in DATA.items():
                achievement_dict['tags'] = [value for key, value in achievement_dict.items() if 'section' in key]
                achievement_dict['awards'] = [{'type': key, 'amount': value} for key, value in achievement_dict.items() 
                         if key in ['achievementPoints', 'darkCrystals']]
                
                if 'xR1' in achievement_dict:
                    achievement_dict['awards'].append({'type': achievement_dict['xR1'], 'amount': achievement_dict['xR1a']})
                if 'xR2' in achievement_dict:
                    achievement_dict['awards'].append({'type': achievement_dict['xR2'], 'amount': achievement_dict['xR2a']})
                if 'xR3' in achievement_dict:
                    achievement_dict['awards'].append({'type': achievement_dict['xR3'], 'amount': achievement_dict['xR3a']})

                self.cache[lang].update({achievement_id.lower(): Achievement(**achievement_dict, id=achievement_id)})

            return list(self.cache[lang].values())
    