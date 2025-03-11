from typing import TYPE_CHECKING

from unidecode import unidecode

from src.modules._utils import is_str_in_list

if TYPE_CHECKING:
    from src.modules.simulacra.dtos import GetSimulacra
    from src.modules.simulacra.model import SimulacrumSimple


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
