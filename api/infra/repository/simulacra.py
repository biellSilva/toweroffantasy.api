import json
from pathlib import Path
from typing import Any

from api.config import GB_BANNERS
from api.core.exceptions import FileNotFound, LanguageNotFound, VersionNotFound
from api.enums import LANGS, LANGS_CN, VERSIONS
from api.infra.entitys import EntityBase, Simulacra
from api.infra.repository.base_repo import ModelRepository
from api.utils import sort_simulacra


class SimulacraRepo(ModelRepository[EntityBase, Simulacra]):
    cache = {}

    def __init__(self) -> None:
        super().__init__(
            model_base=EntityBase,
            model=Simulacra,
            class_base=SimulacraRepo,
            repo_name="imitations",
        )

        self.LINK_DATA: dict[str, dict[str, str | None]] = json.loads(
            Path("api/infra/database/imitation_links.json").read_bytes()
        )

    async def get_all(
        self, lang: LANGS | LANGS_CN | str, version: VERSIONS
    ) -> list[Simulacra]:
        if version in self.cache:
            if lang in self.cache[version]:
                return list(self.cache[version][lang].values())

        VERSION_PATH = Path(f"api/infra/database/{version}")
        if not VERSION_PATH.exists():
            raise VersionNotFound(version)

        LANG_PATH = Path(VERSION_PATH, lang)
        if not LANG_PATH.exists():
            raise LanguageNotFound(lang, version)

        FILEPATH = Path(LANG_PATH, f"{self.repo_name}.json")
        if not FILEPATH.exists():
            raise FileNotFound(self.repo_name, lang, version)

        UNLOCKABLES: dict[
            str, dict[str, list[dict[str, str | int | dict[str, str]]]]
        ] = json.loads(Path(LANG_PATH, "unlockables.json").read_bytes())

        DATA: dict[str, dict[str, Any]] = json.loads(FILEPATH.read_bytes())

        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        for key_id, value_dict in DATA.items():
            if "L1" in key_id or "cn-only" in value_dict["version"].lower():
                continue

            if version == "global":
                value_dict["banners"] = [
                    banner
                    for banner in GB_BANNERS
                    if banner.simulacrumId and banner.simulacrumId == key_id.lower()
                ]
                if value_dict["banners"]:
                    value_dict["isReleased"] = value_dict["banners"][-1].isReleased

                if unlockable := UNLOCKABLES.get(key_id.lower()):
                    __unlockables: list[dict[str, Any]] = []

                    for dict_ in unlockable["unlockables"]:
                        _unlockables: dict[str, Any] = {"need": dict_["stage"]}
                        if text := dict_.get("text"):
                            if "award" not in dict_:

                                type_, name = str(text).split(":", 1)
                                _unlockables.update({"type": type_, "name": name})

                                if _ := dict_.get("trait"):
                                    for awake in value_dict["awakening"]:
                                        if awake["need"] == dict_["stage"]:
                                            _unlockables.update({"icon": awake["icon"]})
                            else:
                                type_, _ = str(text).split(":", 1)

                                icon = dict_["award"]["icon"]

                                if "name" in dict_["award"]:
                                    name = dict_["award"]["name"]
                                else:
                                    name = "King"

                                _unlockables.update(
                                    {"type": type_, "name": name, "icon": icon}
                                )

                        __unlockables.append(_unlockables)
                    value_dict["awakening"] = __unlockables

            if version == "china":
                CN_TRAITS: dict[str, list[dict[str, str | int]]] = json.loads(
                    Path(LANG_PATH, "traits.json").read_bytes()
                )
                value_dict["awakening"] = CN_TRAITS.get(key_id.lower(), [])

            if value_dict.get("id", None):
                self.cache[version][lang].update(
                    {key_id.lower(): Simulacra(**value_dict)}
                )

            else:
                self.cache[version][lang].update(
                    {key_id.lower(): Simulacra(**value_dict, id=key_id)}
                )

        self.cache[version][lang] = {
            i.id: i
            for i in list(
                sorted(list(self.cache[version][lang].values()), key=sort_simulacra)
            )
        }

        return list(self.cache[version][lang].values())
