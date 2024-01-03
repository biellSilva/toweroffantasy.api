
import json

from pathlib import Path
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.repository.item import ItemRepo

from api.infra.entitys import Weapon, EntityBase
from api.infra.entitys.meta import MetaData

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
        
        self.__ITEMS_REPO = ItemRepo()

        self.META_GB: dict[str, dict[str, list[Any]]] = json.loads(Path('api/infra/database/global/meta.json').read_bytes())
        self.DESC_VALUES: dict[str, list[float]] = json.loads(Path('api/infra/database/global/weaponskillnumbers.json').read_bytes())

        self.__weapon_mats: dict[str, list[list[dict[str, str | int | None]]]] = json.loads(Path(f'api/infra/database/global/weaponUpgrade.json').read_bytes())


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
        STAT_VALUES: dict[str, dict[str, str]] = json.loads(Path(f'api/infra/database/global/{lang}/stats.json').read_bytes())

        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        for key_id, value_dict in DATA.items():
            weaponEffects: list[dict[str, str]] = []

            if advancements := value_dict.get('advancements', []):
                if description := advancements[0].get('description', None):
                    if '*:' in description:
                        weaponEffect = description.split('\r\n')
                        
                        for i in weaponEffect:
                            if i == '':
                                continue
                            key, value_ = i.split('*:', 1)
                            key = key.replace('*', '').replace('\n', '').replace('\r', '')
                            value_ = value_.replace('\n', '').replace('\r', '').replace(' ', '', 1)
                            weaponEffects.append({'title': key, 'description': value_})

                    else:
                        if value_dict['id'].lower() == 'fan_superpower':
                            weaponEffects.append({'title': 'Weapon\'s Master', 'description': description.replace('\n', ' ').replace('\r', '')})

                        else:
                            weaponEffects.append({'title': 'Unknown', 'description': description.replace('\n', ' ').replace('\r', '')})

            value_dict.update({
                    'WeaponEffects': weaponEffects, 
                    'Shatter': value_dict['advancements'][0]['shatter'],
                    'Charge': value_dict['advancements'][0]['charge']
                })
            
            for i in value_dict.get('baseStats', []):
                if stats_data := STAT_VALUES.get(i.get('PropName'), None):
                    i.update(stats_data)

            if len(value_dict['advancements']) == 7:
                value_dict['advancements'].pop(0)

            if version == 'global':
                value_dict['Meta'] = self.META_GB.get(key_id.lower(), MetaData())
                value_dict['banners'] = [banner for banner in GB_BANNERS if banner.weaponId and banner.weaponId == key_id.lower()]
                
                if upgrade_obj := self.__weapon_mats.get(value_dict['weaponUpgradeId'], None):
                    for i in upgrade_obj:
                        for j in i:
                            if mat_id := j.get('mat_id', None):
                                if isinstance(mat_id, str) and mat_id.lower() != "none":
                                    if item_obj := await self.__ITEMS_REPO.get(EntityBase(id=mat_id), lang=lang, version=version):
                                        j.update(item_obj.model_dump())

                    value_dict['upgradeMats'] = {'id': value_dict['weaponUpgradeId'], 'items': upgrade_obj}
                
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