from typing import TYPE_CHECKING

from src.infra.models.relics import RawRelic
from src.utils import version_to_float

if TYPE_CHECKING:
    from src.domain.models.relics import Relic


def ignore_relic(dict_: RawRelic) -> bool:
    if "cn-only" in dict_["version"].lower():
        return True
    return False


def relic_advanc_rework(advanc: list[dict[str, str]]) -> list[str]:
    return [value for i in advanc for key, value in i.items() if not key == "id"]


def sort_relics(relics: dict[str, "Relic"]) -> dict[str, "Relic"]:
    def __sort(relic: "Relic") -> tuple[float, float, str]:

        if relic.version and "only" not in relic.version.lower():
            return -relic.rarity, -version_to_float(relic.version), relic.name

        return -relic.rarity, 0, relic.name

    return {relic.id: relic for relic in sorted(list(relics.values()), key=__sort)}
