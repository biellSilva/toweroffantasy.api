from typing import TYPE_CHECKING, Any

from src.config.sorter import WEAPON_SORT_ORDER
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM
from src.infra.models.weapons import RawWeapon
from src.infra.models.weapons.extra import RawStatConverted
from src.infra.repository.items.china import ItemsChinaRepository
from src.infra.repository.items.global_ import ItemsGlobalRepository

if TYPE_CHECKING:
    from src.domain.models.weapons import Weapon


def ignore_weapon(dict_: RawWeapon) -> bool:
    if "cn-only" in dict_["version"].lower():
        return True

    return False


def weapon_fix_minor_issues(dict_: RawWeapon) -> RawWeapon:

    if dict_["id"].lower() in ("lances_ice", "ayanamirei_thunder"):
        dict_["element"] = "ThunderIce"

    elif dict_["id"].lower() in ("blevi_thunder"):
        dict_["element"] = "IceThunder"

    elif dict_["id"].lower() in ("paradox_fire", "dfishchess_fire"):
        dict_["element"] = "FlamePhysics"

    elif dict_["id"].lower() in ("killknife_physic", "zeke_physic", "asuka_physic"):
        dict_["element"] = "PhysicsFlame"

    else:
        pass

    return dict_


def shatter_or_charge_classifier(number: float) -> str:
    if number >= 15:
        return "SS"
    elif number >= 10.01:
        return "S"
    elif number >= 8:
        return "A"
    elif number >= 4:
        return "B"
    else:
        return "C"


def shatter_or_charge_setter(value: float) -> dict[str, str | float | int]:
    return {"tier": shatter_or_charge_classifier(value), "value": value}


def weapon_convert_stat(dict_: RawWeapon) -> list[RawStatConverted]:
    return [
        {
            "id": value["stat"]["id"],
            "name": value["stat"]["name"],
            "icon": value["stat"]["icon"],
            "value": value["value"],
            "upgradeProp": dict_["upgradeProps"][0][i],
        }
        for i, value in enumerate(dict_["stats"])
    ]


async def weapon_upgrade_mats(
    dict_: RawWeapon,
    lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
    WEAPON_MATS: dict[str, Any],
    WEAPON_EXP_REQUIRED_LEVELS: dict[str, Any],
    ITEM_REPO: ItemsGlobalRepository | ItemsChinaRepository,
) -> RawWeapon:

    def get_material(mat_id: str):
        if upgrade_obj := WEAPON_MATS.get(dict_["weaponUpgradeId"], None):
            return upgrade_obj

        for key, value in WEAPON_MATS.items():
            if key.lower() == mat_id.lower():
                return value

        return None

    if upgrade_obj := get_material(dict_["weaponUpgradeId"]):
        if upgrade_exp_require := WEAPON_EXP_REQUIRED_LEVELS.get(
            dict_["id"].lower(), None
        ):
            for ind, level in enumerate(upgrade_obj):
                if "requiredExp" not in level:
                    for item in level:
                        if mat_id := item.get("mat_id", None):
                            if mat_id.lower() != "none":
                                if item_obj := await ITEM_REPO.find_by_id(
                                    mat_id.lower(), lang=lang  # type: ignore
                                ):
                                    item.update(**item_obj.model_dump())

                        ind_start, ind_end = (ind * 10) - 10, ind * 10

                        upgrade_obj[ind] = {
                            "requiredExp": sum(
                                upgrade_exp_require[
                                    (
                                        ind_start if ind_start > 0 else 0
                                    ) : ind_end  # noqa: E203
                                ]
                            ),
                            "mats": level,
                        }

    dict_["upgradeMats"] = {
        "id": dict_["weaponUpgradeId"],
        "levels": upgrade_obj,
    }

    return dict_


def weapon_skill_values(dict_: RawWeapon, DESC_VALUES: dict[str, Any]) -> RawWeapon:
    for type_skill, skill_list in dict_["skills"].items():
        for i, item in enumerate(skill_list):
            if skill_id := item.get("id", None):
                values: list[list[float]] = []
                for _id in DESC_VALUES:
                    if str(skill_id + "_").lower() in _id.lower():
                        values.append(DESC_VALUES[_id])

                dict_["skills"][type_skill][i]["values"] = values

    return dict_


def sort_weapons(weapons: dict[str, "Weapon"]) -> dict[str, "Weapon"]:
    def __sort(weapon: "Weapon") -> tuple[int, int]:
        if weapon.rarity == 5:
            if weapon.banners:
                return -1, -weapon.banners[-1].bannerNumber
            else:
                if weapon.id in WEAPON_SORT_ORDER:
                    return -1, WEAPON_SORT_ORDER.index(weapon.id)
                else:
                    return -1, 0

        elif weapon.rarity == 4:
            if weapon.banners:
                return 1, -weapon.banners[-1].bannerNumber
            else:
                if weapon.id in WEAPON_SORT_ORDER:
                    return 1, WEAPON_SORT_ORDER.index(weapon.id)
                else:
                    return 1, 0

        elif weapon.rarity == 3:
            if weapon.banners:
                return 2, -weapon.banners[-1].bannerNumber
            else:
                if weapon.id in WEAPON_SORT_ORDER:
                    return 2, WEAPON_SORT_ORDER.index(weapon.id)
                else:
                    return 2, 0

        return 3, 0

    return {weapon.id: weapon for weapon in sorted(list(weapons.values()), key=__sort)}
