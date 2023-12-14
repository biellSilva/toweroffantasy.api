
import json

from pathlib import Path
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Weapon, EntityBase

from api.core.exceptions import VersionNotFound, LanguageNotFound, FileNotFound, ItemNotFound

from api.enums import LANGS, LANGS_CN, VERSIONS
from api.utils import sort_weapons, place_numbers
from api.config import GB_BANNERS


class WeaponRepo(ModelRepository[EntityBase, Weapon]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Weapon, 
                         class_base=WeaponRepo,
                         repo_name='weapons')
        
        self.META_GB: dict[str, dict[str, list[Any]]] = json.loads(Path('api/infra/database/global/meta.json').read_bytes())
        self.DESC_VALUES: dict[str, list[float]] = json.loads(Path('api/infra/database/global/weaponskillnumbers.json').read_bytes())


    async def get(self, model: EntityBase, lang: LANGS | LANGS_CN | str, version: VERSIONS, graphql: bool = False) -> Weapon:
        if version in self.class_base.cache:
            if lang in self.class_base.cache[version]:
                if model.id in self.class_base.cache[version][lang]:
                    if graphql:
                        return self.class_base.cache[version][lang][model.id]
                    else:
                        return place_numbers(Weapon(**self.class_base.cache[version][lang][model.id].model_dump(by_alias=True)))
                else:
                    raise ItemNotFound(model.id, lang, version)

        await self.get_all(lang=lang, version=version)
        return await self.get(model, lang, version)


    async def get_all(self, lang: LANGS | LANGS_CN | str, version: VERSIONS, graphql: bool = False) -> list[Weapon]:
        
        if version in self.class_base.cache:
            if lang in self.class_base.cache[version]:
                if graphql:
                    return list(self.class_base.cache[version][lang].values())
                else:
                    return [place_numbers(Weapon(**value.model_dump(by_alias=True))) for value in self.class_base.cache[version][lang].values()]

        VERSION_PATH = Path(f'api/infra/database/{version}')
        if not VERSION_PATH.exists():
            raise VersionNotFound(version)
        
        LANG_PATH = Path(VERSION_PATH, lang)
        if not LANG_PATH.exists():
            raise LanguageNotFound(lang, version)

        FILEPATH = Path(LANG_PATH, f'{self.repo_name}.json')
        if not FILEPATH.exists():
            raise FileNotFound(self.repo_name, lang, version)

        DATA: dict[str, dict[str, Any]] = json.loads(FILEPATH.read_bytes())

        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        for key_id, value_dict in DATA.items():
            weaponEffects: list[dict[str, str]] = []

            if advancements := value_dict.get('advancements', []):
                if description := advancements[0].get('description', None):
                    if '*:' in description:
                        weaponEffect = description.split('\r', 1)

                        for i in weaponEffect:
                            key, value_ = i.split('*:', 1)
                            key = key.replace('*', '').replace('\n', '').replace('\r', '')
                            value_ = value_.replace('\n', '').replace('\r', '').replace(' ', '', 1)
                            weaponEffects.append({'title': key, 'description': value_})

                    else:
                        if value_dict['id'].lower() == 'fan_superpower':
                            weaponEffects.append({'title': 'Altered Damage', 'description': description.replace('\n', ' ').replace('\r', '')})

                        else:
                            weaponEffects.append({'title': 'Unknown', 'description': description.replace('\n', ' ').replace('\r', '')})

            value_dict.update({
                    'WeaponEffects': weaponEffects, 
                    'Shatter': value_dict['advancements'][0]['shatter'],
                    'Charge': value_dict['advancements'][0]['charge']
                })
            

            # if len(value_dict['advancements']) == 7:
            #     value_dict['advancements'].pop(0)
            

            if version == 'global':
                value_dict['Meta'] = self.META_GB.get(key_id.lower(), None)
                value_dict['banners'] = [banner for banner in GB_BANNERS if banner.weaponId and banner.weaponId == key_id.lower()]

            for type_skill, skill_list in value_dict['skills'].items():
                skill_list: list[dict[str, Any]]
                for i, item in enumerate(skill_list):
                    if skill_id := item.get('id', None):
                        values: list[list[float]] = []
                        for _id in self.DESC_VALUES:
                            if str(skill_id + '_').lower() in _id.lower():
                                values.append(self.DESC_VALUES[_id])
                    
                        value_dict['skills'][type_skill][i]['values'] = values


            if value_dict.get('id', None):
                self.cache[version][lang].update({key_id.lower(): Weapon(**value_dict)})
            else:
                self.cache[version][lang].update({key_id.lower(): Weapon(**value_dict, id=key_id)})

        self.cache[version][lang] = {i.id: i for i in list(sorted(list(self.cache[version][lang].values()), key=sort_weapons))}

        if graphql:
            return list(self.class_base.cache[version][lang].values())
        else:
            return [place_numbers(Weapon(**value.model_dump(by_alias=True))) for value in self.class_base.cache[version][lang].values()]