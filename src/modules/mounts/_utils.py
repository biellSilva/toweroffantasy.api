from typing import TYPE_CHECKING

from unidecode import unidecode

from src.modules._utils import is_str_in_list

if TYPE_CHECKING:
    from src.modules.mounts.dtos import GetMounts
    from src.modules.mounts.model import MountSimple


def filter_mounts(data: "MountSimple", /, *, params: "GetMounts") -> bool:
    if (
        params.name
        and unidecode(params.name).lower() not in unidecode(data.name).lower()
    ):
        return False

    includes = [
        (params.include_ids, data.id, True),
        (params.include_mount_type, data.mount_type, True),
        (params.include_quality, data.quality, True),
    ]
    excludes = [
        (params.exclude_ids, data.id, True),
        (params.exclude_mount_type, data.mount_type, True),
        (params.exclude_quality, data.quality, True),
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
