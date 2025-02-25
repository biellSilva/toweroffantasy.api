from typing import TYPE_CHECKING

from unidecode import unidecode

from src._utils import is_str_in_list

if TYPE_CHECKING:
    from src.modules.simulacra.dtos import GetSimulacra
    from src.modules.simulacra.model import SimulacrumSimple


def filter_simulacra(
    data: "SimulacrumSimple",
    /,
    *,
    params: "GetSimulacra",
    include_id: list[str] | None,
    exclude_id: list[str] | None,
    include_sex: list[str] | None,
    exclude_sex: list[str] | None,
    include_rarity: list[str] | None,
    exclude_rarity: list[str] | None,
) -> bool:
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
        (include_id, data.id, True),
        (include_rarity, data.rarity, True),
        (include_sex, data.sex, True),
    ]
    excludes = [
        (exclude_id, data.id, True),
        (exclude_rarity, data.rarity, True),
        (exclude_sex, data.sex, True),
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
