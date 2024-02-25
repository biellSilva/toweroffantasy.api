import json

from pathlib import Path
from typing import Any

from api.infra.repository.base_repo import ModelRepository
from api.infra.entitys import Achievement, EntityBase

from api.core.exceptions import VersionNotFound, LanguageNotFound, FileNotFound


class AchievementRepo(ModelRepository[EntityBase, Achievement]):
    cache = {}
    __load_all_data__: bool = False

    def __init__(self) -> None:
        super().__init__(
            model_base=EntityBase,
            model=Achievement,
            class_base=AchievementRepo,
            repo_name="achievements",
        )

    async def get_all(self, lang: str, version: str) -> list[Achievement]:
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

        DATA: dict[str, dict[str, Any]] = json.loads(FILEPATH.read_bytes())

        if version not in self.cache:
            self.cache.update({version: {}})

        if lang not in self.cache[version]:
            self.cache[version].update({lang: {}})

        for achievement_id, achievement_dict in DATA.items():
            achievement_dict["tags"] = [
                value for key, value in achievement_dict.items() if "section" in key
            ]

            rewards: list[dict[str, Any]] = []

            for reward in achievement_dict["achievementRewards"]:
                rewards.append(reward)

            for reward_2 in achievement_dict["extraRewards"]:
                rewards.append(reward_2)

            achievement_dict["rewards"] = rewards

            if achievement_dict.get("id", None):
                self.cache[version][lang].update(
                    {achievement_id.lower(): self.model(**achievement_dict)}
                )
            else:
                self.cache[version][lang].update(
                    {
                        achievement_id.lower(): self.model(
                            **achievement_dict, id=achievement_id
                        )
                    }
                )

        return list(self.cache[version][lang].values())
