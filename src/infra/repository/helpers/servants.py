from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.servants import SmartServant


def sort_servants(servants: dict[str, "SmartServant"]) -> dict[str, "SmartServant"]:
    def __sort(servant: "SmartServant") -> tuple[float, str]:
        return -servant.rarity, servant.name

    return {
        servant.id: servant for servant in sorted(list(servants.values()), key=__sort)
    }
