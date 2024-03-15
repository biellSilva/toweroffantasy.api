from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.outfits import Outfit


def sort_outfits(outfits: dict[str, "Outfit"]) -> dict[str, "Outfit"]:
    def __sort(outfit: "Outfit") -> tuple[str, str]:
        if outfit.name:
            return outfit.type, outfit.name

        return outfit.type, outfit.id

    return {outfit.id: outfit for outfit in sorted(list(outfits.values()), key=__sort)}
