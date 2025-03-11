from typing import TYPE_CHECKING

from unidecode import unidecode

from src.modules._utils import is_str_in_list

if TYPE_CHECKING:
    from src.modules.weapons.dtos import GetWeapons
    from src.modules.weapons.model import WeaponSimple


def filter_weapons(data: "WeaponSimple", /, *, params: "GetWeapons") -> bool:  # noqa: C901
    if params.is_limited is not None and data.is_limited != params.is_limited:
        return False

    if params.is_fate is not None and data.is_fate != params.is_fate:
        return False

    if params.is_warehouse is not None and data.is_warehouse != params.is_warehouse:
        return False

    if (
        params.charge_tier is not None
        and data.charge.tier.lower() != params.charge_tier.lower()
    ):
        return False

    if (
        params.charge_value is not None
        and int(data.charge.value) != params.charge_value
    ):
        return False

    if (
        params.shatter_tier is not None
        and data.shatter.tier.lower() != params.shatter_tier.lower()
    ):
        return False

    if (
        params.shatter_value is not None
        and int(data.shatter.value) != params.shatter_value
    ):
        return False

    if (
        params.name
        and unidecode(params.name).lower() not in unidecode(data.name).lower()
    ):
        return False

    includes = [
        (params.include_ids, data.id, True),
        (params.include_elements, data.element.id, True),
        (params.include_categories, data.category.id, True),
        (params.include_rarities, data.rarity, True),
        (params.include_qualities, data.quality, True),
    ]
    excludes = [
        (params.exclude_ids, data.id, True),
        (params.exclude_elements, data.element.id, True),
        (params.exclude_categories, data.category.id, True),
        (params.exclude_rarities, data.rarity, True),
        (params.exclude_qualities, data.quality, True),
    ]

    for inc, param, equals in includes:
        if inc and not is_str_in_list(param, inc, equals=equals):
            return False

    for exc, param, equals in excludes:
        if exc and is_str_in_list(param, exc, equals=equals):
            return False

    return True
