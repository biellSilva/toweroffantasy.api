from typing import TYPE_CHECKING, Any

from src.config.sorter import WEAPON_SORT_ORDER
from src.enums import LANGS_CHINA_ENUM, LANGS_GLOBAL_ENUM, VERSIONS_ENUM
from src.infra.models.weapons import RawWeapon
from src.infra.models.weapons.extra import RawStatConverted
from src.infra.repository.items import ItemsRepository

if TYPE_CHECKING:
    from src.domain.models.weapons import Weapon


def ignore_weapon(dict_: RawWeapon) -> bool:
    if "cn-only" in dict_["version"].lower():
        return True

    return False


def weapon_fix_minor_issues(dict_: RawWeapon) -> RawWeapon:
    if dict_["id"].lower() == "blevi_thunder":
        dict_["element"] = "IceThunder"

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
    version: VERSIONS_ENUM,
    lang: LANGS_GLOBAL_ENUM | LANGS_CHINA_ENUM,
    __WEAPON_MATS: dict[str, Any],
    __WEAPON_EXP_REQUIRED_LEVELS: dict[str, Any],
    __ITEM_REPO: ItemsRepository,
) -> RawWeapon:
    if upgrade_obj := __WEAPON_MATS.get(dict_["weaponUpgradeId"], None):
        if upgrade_exp_require := __WEAPON_EXP_REQUIRED_LEVELS.get(
            dict_["id"].lower(), None
        ):
            for ind, level in enumerate(upgrade_obj):
                if "requiredExp" not in level:
                    for item in level:
                        if mat_id := item.get("mat_id", None):
                            if mat_id.lower() != "none":
                                if item_obj := await __ITEM_REPO.find_by_id(
                                    mat_id.lower(), version=version, lang=lang
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

        else:
            for ind, level in enumerate(upgrade_obj):
                for item in level:
                    if mat_id := item.get("mat_id", None):
                        if mat_id.lower() != "none":
                            if item_obj := await __ITEM_REPO.find_by_id(
                                id=mat_id,
                                lang=lang,
                                version=version,
                            ):
                                item.update(**item_obj.model_dump())

                    upgrade_obj[ind] = {
                        "requiredExp": 0,
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