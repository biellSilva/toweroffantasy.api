from typing import TYPE_CHECKING

from src.infra.models.mounts import RawMount

if TYPE_CHECKING:
    from src.domain.models.mounts import Mount


def ignore_mounts(dict_: RawMount) -> bool:
    if "version" in dict_ and "cn-only" in dict_["version"].lower():
        return True
    return False


def sort_mounts(mounts: dict[str, "Mount"]) -> dict[str, "Mount"]:
    def __sort(mount: "Mount") -> tuple[float, float]:
        if mount.version.lower() in ("cn-only", "ps-only"):
            return 0, -mount.rarity

        return -float(mount.version), -mount.rarity

    return {mount.id: mount for mount in sorted(list(mounts.values()), key=__sort)}
