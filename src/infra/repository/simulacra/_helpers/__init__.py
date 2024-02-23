from typing import TYPE_CHECKING
from src.config.sorter import SIMULACRA_SORT_ORDER
from src.infra.models.simulacra import RawSimulacra

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
        if simulacrum.rarity == 5:
            if simulacrum.banners:
                return -1, -simulacrum.banners[-1].bannerNumber
            elif simulacrum.id == "imitation_33":
                return -1, -70.9
            else:
                if simulacrum.id in SIMULACRA_SORT_ORDER:
                    return -1, SIMULACRA_SORT_ORDER.index(simulacrum.id)
                else:
                    return -1, 0

        elif simulacrum.rarity == 4:
            if simulacrum.banners:
                return 1, -simulacrum.banners[-1].bannerNumber
            else:
                if simulacrum.id in SIMULACRA_SORT_ORDER:
                    return 1, SIMULACRA_SORT_ORDER.index(simulacrum.id)
                else:
                    return 1, 0

        return 2, 0

    return {
        simulacrum.id: simulacrum
        for simulacrum in sorted(list(simulacra.values()), key=__sort)
    }
