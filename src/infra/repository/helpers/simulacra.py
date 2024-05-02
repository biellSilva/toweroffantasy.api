from typing import TYPE_CHECKING

from src.config.sorter import SIMULACRA_SORT_ORDER
from src.infra.models.simulacra import RawSimulacra
from src.utils import version_to_float

if TYPE_CHECKING:
    from src.domain.models.simulacra import Simulacra


def ignore_simulacra(dict_: RawSimulacra) -> bool:
    if "cn-only" in dict_["version"].lower():
        return True

    if "L1" in dict_["id"]:
        return True

    return False


def sort_simulacra(simulacra: dict[str, "Simulacra"]) -> dict[str, "Simulacra"]:
    def __sort(simulacrum: "Simulacra") -> tuple[float, float]:

        if simulacrum.banners:
            return -simulacrum.rarity, -simulacrum.banners[-1].bannerNumber

        if simulacrum.id in SIMULACRA_SORT_ORDER:
            return -simulacrum.rarity, SIMULACRA_SORT_ORDER.index(simulacrum.id)

        if simulacrum.version and 'only' not in simulacrum.version.lower():
            return -simulacrum.rarity, -version_to_float(simulacrum.version)

        return -simulacrum.rarity, 0

    return {
        simulacrum.id: simulacrum
        for simulacrum in sorted(list(simulacra.values()), key=__sort)
    }
