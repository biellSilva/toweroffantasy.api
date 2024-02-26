import json
from pathlib import Path

from src.domain.errors.http import DataIncompleteErr
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM
from src.infra.models.simulacra import RawSimulacra
from src.infra.models.simulacra._helpers.unlockables import RawUnlockables
from src.infra.models.simulacra.extra import RawAwakening


def add_unlockables(
    dict_: RawSimulacra,
    version: VERSIONS_ENUM,
    lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
) -> RawSimulacra:
    UNLOCKABLES_PATH = Path("./src/infra/database", version, lang, "unlockables.json")

    if not UNLOCKABLES_PATH.exists():
        raise DataIncompleteErr

    UNLOCKABLES_DATA: dict[str, RawUnlockables] = json.loads(
        UNLOCKABLES_PATH.read_bytes()
    )

    if unlockable := UNLOCKABLES_DATA.get(dict_["id"].lower()):
        __unlockables: list[RawAwakening] = []

        for unlock_dict in unlockable["unlockables"]:
            name: str | None = None
            icon: str | None = None
            stage: int = unlock_dict["stage"]
            trait: str | None = None

            if text := unlock_dict.get("text"):
                if "award" not in unlock_dict:
                    name = text

                    if _ := unlock_dict.get("trait"):
                        for awake in dict_["awakening"]:
                            if awake["need"] == unlock_dict["stage"]:
                                trait = awake["description"]
                                icon = awake["icon"]
                else:

                    icon = unlock_dict["award"]["icon"]

                    if "name" in unlock_dict["award"]:
                        name = unlock_dict["award"]["name"]

                    else:
                        name = "King"

            __unlockables.append(
                {"name": name, "description": trait, "icon": icon, "need": stage}
            )
        dict_["awakening"] = __unlockables

    return dict_
