from typing import TYPE_CHECKING

from unidecode import unidecode

from src.modules._utils import is_str_in_list, rarity_to_int

if TYPE_CHECKING:
    from src.modules.simulacra.dtos import GetSimulacra
    from src.modules.simulacra.model import Simulacrum, SimulacrumSimple


def sort_simulacra(
    data: "Simulacrum",
) -> tuple[int, int, bool, int, str]:
    if not data.banners:
        return (
            0,
            0,
            data.is_limited or data.no_weapon,
            -rarity_to_int(data.rarity),
            data.name,
        )

    return (
        -int(data.banners[-1].start_at.timestamp()),
        -int(data.banners[-1].end_at.timestamp()),
        data.is_limited or data.no_weapon,
        -rarity_to_int(data.rarity),
        data.name,
    )


def filter_simulacra(data: "SimulacrumSimple", /, *, params: "GetSimulacra") -> bool:
    if params.is_limited is not None and data.is_limited != params.is_limited:
        return False

    if params.no_weapon is not None and data.no_weapon != params.no_weapon:
        return False

    if (
        params.name
        and unidecode(params.name).lower() not in unidecode(data.name).lower()
    ):
        return False

    includes = [
        (params.include_ids, data.id, True),
        (params.include_rarities, data.rarity, True),
        (params.include_sex, data.sex, True),
    ]
    excludes = [
        (params.exclude_ids, data.id, True),
        (params.exclude_rarities, data.rarity, True),
        (params.exclude_sex, data.sex, True),
    ]

    for include, value, equals in includes:
        if include and not is_str_in_list(
            value,
            include,
            equals=equals,
        ):
            return False

    for exclude, value, equals in excludes:
        if exclude and is_str_in_list(
            value,
            exclude,
            equals=equals,
        ):
            return False

    return True
