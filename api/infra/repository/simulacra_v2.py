import json

from pathlib import Path
from typing import Any

from api.core.exceptions import (
    LanguageNotFound,
    VersionNotFound,
    FileNotFound,
    ItemNotFound,
)

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Simulacra_v2, EntityBase
from api.infra.repository import WeaponRepo, MatricesRepo

from api.enums import LANGS, LANGS_CN, VERSIONS
from api.utils import sort_simulacra, place_numbers_v2
from api.config import GB_BANNERS


class SimulacraV2Repo(ModelRepository[EntityBase, Simulacra_v2]):
    cache = {}

    def __init__(self) -> None:
        super().__init__(
            model_base=EntityBase,
            model=Simulacra_v2,
            class_base=SimulacraV2Repo,
            repo_name="imitations",
        )

        self.WEAPON_REPO = WeaponRepo()
        self.MATRIX_REPO = MatricesRepo()

        self.LINK_DATA: dict[str, dict[str, str | None]] = json.loads(
            Path("api/infra/database/imitation_links.json").read_bytes()
        )

    async def get(
        self,
        model: EntityBase,
        lang: LANGS | LANGS_CN | str,
        version: VERSIONS,
        graphql: bool = False,
    ) -> Simulacra_v2:
        if version in self.cache:
            if lang in self.cache[version]:
                if model.id in self.cache[version][lang]:
                    if graphql:
                        return self.cache[version][lang][model.id]
                    else:
                        return place_numbers_v2(
                            Simulacra_v2(
                                **self.cache[version][lang][model.id].model_dump(
                                    by_alias=True
                                )
                            )
                        )
                else:
                    raise ItemNotFound(model.id, lang, version)

        await self.get_all(lang, version, graphql)
        return await self.get(model, lang, version, graphql)

    async def get_all(
        self, lang: LANGS | LANGS_CN | str, version: VERSIONS, graphql: bool = False
    ) -> list[Simulacra_v2]:
        if version in self.cache:
            if lang in self.cache[version]:
                if graphql:
                    return list(self.cache[version][lang].values())
                else:
                    return [
                        place_numbers_v2(
                            Simulacra_v2(**value.model_dump(by_alias=True))
                        )
                        for value in self.cache[version][lang].values()
                    ]

        VERSION_PATH = Path(f"api/infra/database/{version}")
        if not VERSION_PATH.exists():
            raise VersionNotFound(version)

        LANG_PATH = Path(VERSION_PATH, lang)
        if not LANG_PATH.exists():
            raise LanguageNotFound(lang, version)

        FILEPATH = Path(LANG_PATH, f"{self.repo_name}.json")
        if not FILEPATH.exists():
            raise FileNotFound(self.repo_name, lang, version)

        DATA: dict[str, dict[str, Any]] = json.loads(FILEPATH.read_bytes())

        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        for key_id, value_dict in DATA.items():
            if "L1" in key_id:
                continue

            if version == "global":
                value_dict["banners"] = [
                    banner
                    for banner in GB_BANNERS
                    if banner.simulacrumId and banner.simulacrumId == key_id.lower()
                ]
                if value_dict["banners"]:
                    value_dict["isReleased"] = value_dict["banners"][-1].isReleased

            if WEAPON_ID := value_dict.get("weaponId", None):
                if WEAPON_ID and WEAPON_ID not in ("none", "null"):
                    if WEAPON := await self.WEAPON_REPO.get(
                        EntityBase(id=WEAPON_ID),
                        lang=lang,
                        version=VERSIONS("global"),
                        graphql=True,
                    ):
                        value_dict["weapon"] = WEAPON

            if MATRIX_ID := value_dict.get("matrixId", None):
                if MATRIX_ID and MATRIX_ID not in ("none", "null"):
                    if MATRIX := await self.MATRIX_REPO.get(
                        EntityBase(id=MATRIX_ID), lang=lang, version=VERSIONS("global")
                    ):
                        value_dict["matrix"] = MATRIX

            if value_dict.get("id", None):
                self.cache[version][lang].update(
                    {key_id.lower(): Simulacra_v2(**value_dict)}
                )

            else:
                self.cache[version][lang].update(
                    {key_id.lower(): Simulacra_v2(**value_dict, id=key_id)}
                )

        self.cache[version][lang] = {
            i.id: i
            for i in list(
                sorted(list(self.cache[version][lang].values()), key=sort_simulacra)
            )
        }

        if graphql:
            return list(self.cache[version][lang].values())
        else:
            return [
                place_numbers_v2(Simulacra_v2(**value.model_dump(by_alias=True)))
                for value in self.cache[version][lang].values()
            ]
