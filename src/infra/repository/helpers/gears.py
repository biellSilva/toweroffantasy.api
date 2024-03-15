from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    from src.domain.models.gears import Gear


def ignore_gears(dict_: dict[str, Any]) -> bool:
    if "tupo" in dict_["id"].lower():
        return True
    return False


def sort_gears(gears: dict[str, "Gear"]) -> dict[str, "Gear"]:
    def __sort(gear: "Gear") -> tuple[float, str, str]:
        return -gear.rarity, gear.type, gear.name

    return {gear.id: gear for gear in sorted(list(gears.values()), key=__sort)}
