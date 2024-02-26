from src.infra.models.banners import RawBanner
from src.utils.banners import str_to_datetime


def sort_banners_without_number(dict_: RawBanner) -> tuple[float, float, float]:
    dict_["startDate"] = str_to_datetime(dict_["start"])
    dict_["endDate"] = str_to_datetime(dict_["end"])

    if dict_["is_rerun"]:
        return -dict_["startDate"].timestamp(), -1, -dict_["endDate"].timestamp()
    else:
        return -dict_["startDate"].timestamp(), 1, -dict_["endDate"].timestamp()
