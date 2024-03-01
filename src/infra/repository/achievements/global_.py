import json
from pathlib import Path
from typing import Any

from src.domain.errors.http import LangNotFoundErr
from src.domain.models.achievements import Achievement
from src.enums import LANGS_GLOBAL_ENUM
from src.infra.models.achievements import RawAchievement


class AchievementsGlobalRepository:
    __cache: dict[LANGS_GLOBAL_ENUM, dict[str, Achievement]] = {}

    async def find_by_id(
        self,
        id: str,
        lang: LANGS_GLOBAL_ENUM,
    ) -> Achievement | None:

        if cached_lang := self.__cache.get(lang):
            if achiev := cached_lang.get(id):
                return achiev
            return None

        await self.load_data(lang=lang)

        return await self.find_by_id(id=id, lang=lang)

    async def get_all(self, lang: LANGS_GLOBAL_ENUM) -> list[Achievement]:

        if cached_lang := self.__cache.get(lang):
            return list(cached_lang.values())

        await self.load_data(lang=lang)

        return await self.get_all(lang=lang)

    async def load_data(self, lang: LANGS_GLOBAL_ENUM) -> None:

        if lang not in self.__cache:
            self.__cache.update({lang: {}})

        DATA_PATH = Path("./src/infra/database/global", lang, "achievements.json")

        if not DATA_PATH.exists():
            raise LangNotFoundErr

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
                self.__cache[lang].update(
                    {key_id.lower(): Achievement(**value_dict)}  # type: ignore
                )
            else:
                self.__cache[lang].update(
                    {key_id.lower(): Achievement(**value_dict, id=key_id)}  # type: ignore
                )
