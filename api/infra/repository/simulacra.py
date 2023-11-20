
import json

from pathlib import Path
from typing import Any
from unidecode import unidecode

from api.core.exceptions import LanguageNotFound, VersionNotFound, FileNotFound, ItemNotFound

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Simulacra, EntityBase

from api.enums import LANGS, LANGS_CN, VERSIONS
from api.utils import localized_asset, sort_simulacra
from api.config import GB_BANNERS


class SimulacraRepo(ModelRepository[EntityBase, Simulacra]):
    cache = {}

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Simulacra, 
                         class_base=SimulacraRepo,
                         repo_name='imitations')
        
        self.GB_LINK: dict[str, dict[str, str | None]] = json.loads(Path('api/infra/database/global/imitation_links.json').read_bytes())


    async def get_by_name(self, name: str, lang: LANGS, version: VERSIONS) -> Simulacra:
        name_unidecoded = unidecode(name).lower()
        if version in self.class_base.cache:
            if lang in self.class_base.cache[version]:
                for model in self.cache[version][lang].values():
                    model_name = unidecode(model.name).lower()
                    if (model_name == name_unidecoded or 
                        model_name.replace(' ', '-') == name_unidecoded or
                        model_name.replace(' ', '_') == name_unidecoded):
                        return model
                
                raise ItemNotFound(name_unidecoded, lang, version)

        await self.get_all(lang=lang, version=version)
        return await self.get_by_name(name, lang, version)


    async def get_all(self, lang: LANGS | LANGS_CN, version: VERSIONS) -> list[Simulacra]:
        if version in self.class_base.cache:
            if lang in self.class_base.cache[version]:
                return list(self.class_base.cache[version][lang].values())

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
            if 'L1' in key_id:
                continue

            if version == 'global':
                value_dict['rating'] = localized_asset(value_dict['rating'], LANGS(lang))
                value_dict['assets']['NamePicture'] = localized_asset(value_dict['assets']['NamePicture'], LANGS(lang))
                value_dict['banners'] = [banner for banner in GB_BANNERS if banner.imitation_id and banner.imitation_id == key_id.lower()]

                if LINK := self.GB_LINK.get(key_id.lower(), None):
                    value_dict['matrixID'] = LINK.get('matrice', None)

            if value_dict.get('id', None):
                self.cache[version][lang].update({key_id.lower(): Simulacra(**value_dict)})

            else:
                self.cache[version][lang].update({key_id.lower(): Simulacra(**value_dict, id=key_id)})

        self.cache[version][lang] = {i.id: i for i in list(sorted(list(self.cache[version][lang].values()), key=sort_simulacra))}

        return list(self.cache[version][lang].values())
    