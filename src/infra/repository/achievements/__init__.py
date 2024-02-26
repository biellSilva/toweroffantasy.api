import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import DataNotFoundErr
from src.domain.models.achievements import Achievement
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM
from src.infra.models.achievements import RawAchievement


class AchievementsRepository:
    cache: dict[
        VERSIONS_ENUM,
        dict[LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM, dict[str, Achievement]],
    ] = {}

    async def find_by_id(
        self,
        id: str,
        version: VERSIONS_ENUM,
        lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
    ) -> Achievement | None:

        if cached_version := self.cache.get(version):
            if cached_lang := cached_version.get(lang):
                if achiev := cached_lang.get(id):
                    return achiev
                return None

        await self.load_data(version=version, lang=lang)

        return await self.find_by_id(id=id, version=version, lang=lang)

    async def get_all(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> list[Achievement]:
        if cached_version := self.cache.get(version):
            if cached_lang := cached_version.get(lang):
                return list(cached_lang.values())

        await self.load_data(version=version, lang=lang)

        return await self.get_all(version=version, lang=lang)

    async def load_data(
        self, version: VERSIONS_ENUM, lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM
    ) -> None:
        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        DATA_PATH = Path("./src/infra/database", version, lang, "achievements.json")

        if not DATA_PATH.exists():
            raise DataNotFoundErr

        DATA: dict[str, RawAchievement] = json.loads(DATA_PATH.read_bytes())

        for key_id, value_dict in DATA.items():

            value_dict["tags"] = [
                str(value) for key, value in value_dict.items() if "section" in key
            ]

            rewards: list[dict[str, Any]] = []

            for reward in value_dict["achievementRewards"]:
                rewards.append(reward)

            for reward_2 in value_dict["extraRewards"]:
                rewards.append(reward_2)

            value_dict["rewards"] = rewards

            if value_dict.get("id", None):
                self.cache[version][lang].update(
                    {key_id.lower(): Achievement(**value_dict)}  # type: ignore
                )
            else:
                self.cache[version][lang].update(
                    {key_id.lower(): Achievement(**value_dict, id=key_id)}  # type: ignore
                )
