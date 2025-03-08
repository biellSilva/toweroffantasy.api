from unidecode import unidecode


def is_str_in_list(
    param: str,
    list_: list[str],
    *,
    equals: bool = False,
) -> bool:
    if equals:
        return any(
            unidecode(param).lower() == unidecode(item).lower() for item in list_
        )

    return any(unidecode(param).lower() in unidecode(item).lower() for item in list_)


def rarity_to_int(value: str) -> int:
    return {
        "N": 0,
        "R": 1,
        "SR": 2,
        "SSR": 3,
    }[value]


def quality_to_int(value: str) -> int:
    return {
        "COMMON": 0,
        "RARE": 1,
        "EPIC": 2,
        "LEGENDRY": 3,
        "RED": 4,
    }[value]
