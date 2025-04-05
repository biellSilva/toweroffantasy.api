from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.modules.simulacra.dtos import GetSimulacra


def filter_simulacra(params: "GetSimulacra") -> dict[str, Any]:  # noqa: PLR0912 C901
    """Mongo filter for Simulacra."""

    filters: dict[str, Any] = {}

    if params.is_limited is not None:
        filters["is_limited"] = params.is_limited

    if params.no_weapon is not None:
        filters["no_weapon"] = params.no_weapon

    if params.include_ids:
        filters["id"] = {"$in": params.include_ids}

    if params.exclude_ids:
        if "id" in filters:
            filters["id"]["$nin"] = params.exclude_ids
        else:
            filters["id"] = {"$nin": params.exclude_ids}

    if params.include_sex:
        filters["sex"] = {"$in": params.include_sex}

    if params.exclude_sex:
        if "sex" in filters:
            filters["sex"]["$nin"] = params.exclude_sex
        else:
            filters["sex"] = {"$nin": params.exclude_sex}

    if params.include_rarities:
        filters["rarity"] = {"$in": params.include_rarities}

    if params.exclude_rarities:
        if "rarity" in filters:
            filters["rarity"]["$nin"] = params.exclude_rarities
        else:
            filters["rarity"] = {"$nin": params.exclude_rarities}

    return filters
