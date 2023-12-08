
import json

from pathlib import Path
from typing import Any

from api.core.exceptions import LanguageNotFound, VersionNotFound, FileNotFound

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Simulacra_v2, EntityBase
from api.infra.repository import WeaponRepo, MatricesRepo

from api.enums import LANGS, LANGS_CN, VERSIONS
from api.utils import sort_simulacra, localized_asset
from api.config import GB_BANNERS


class SimulacraV2Repo(ModelRepository[EntityBase, Simulacra_v2]):
    cache = {}

    def __init__(self) -> None:
        super().__init__(model_base=EntityBase, 
                         model=Simulacra_v2, 
                         class_base=SimulacraV2Repo,
                         repo_name='imitations')

        self.WEAPON_REPO = WeaponRepo()
        self.MATRIX_REPO = MatricesRepo()
        
        self.LINK_DATA: dict[str, dict[str, str | None]] = json.loads(Path('api/infra/database/imitation_links.json').read_bytes())

    async def get_all(self, lang: LANGS | LANGS_CN | str, version: VERSIONS) -> list[Simulacra_v2]:
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
                value_dict['Banners'] = [banner for banner in GB_BANNERS if banner.simulacrumId and banner.simulacrumId == key_id.lower()]
                value_dict['assetsA0']['descPainting'] = localized_asset(
                    text = value_dict['assetsA0']['descPainting'],
                    lang=LANGS(lang)
                )

                if value_dict.get('assetsA3', None):
                    value_dict['assetsA3']['descPainting'] = localized_asset(
                    text = value_dict['assetsA3']['descPainting'],
                    lang=LANGS(lang)
                )

            if LINK := self.LINK_DATA.get(key_id.lower(), None):
                value_dict['MatrixId'] = LINK.get('matrice', None)
            
            if WEAPON_ID := value_dict.get('weaponId', None):
                if WEAPON_ID and WEAPON_ID not in ('none', 'null'):
                    if WEAPON := await self.WEAPON_REPO.get(EntityBase(id=WEAPON_ID), lang=lang, version=VERSIONS('global')):
                        value_dict['weapon'] = WEAPON
            
            if MATRIX_ID := value_dict.get('MatrixId', None):
                if MATRIX_ID and MATRIX_ID not in ('none', 'null'):
                    if MATRIX := await self.MATRIX_REPO.get(EntityBase(id=MATRIX_ID), lang=lang, version=VERSIONS('global')):
                        value_dict['matrix'] = MATRIX

            if value_dict.get('id', None):
                self.cache[version][lang].update({key_id.lower(): Simulacra_v2(**value_dict)})

            else:
                self.cache[version][lang].update({key_id.lower(): Simulacra_v2(**value_dict, id=key_id)})

        self.cache[version][lang] = {i.id: i for i in list(sorted(list(self.cache[version][lang].values()), key=sort_simulacra))}

        return list(self.cache[version][lang].values())
    