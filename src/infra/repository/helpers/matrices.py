from typing import TYPE_CHECKING

from src.config.sorter import MATRIX_SORT_ORDER
from src.infra.models.matrices import RawMatrix

if TYPE_CHECKING:
    from src.domain.models.matrices import Matrix


def ignore_matrix(dict_: RawMatrix) -> bool:
    if "cn-only" in dict_["version"].lower():
        return True
    return False


def matrix_set_rework(dict_: RawMatrix) -> RawMatrix:
    def _matrice_set_rework(
        rarity: int, sets: list[dict[str, str]]
    ) -> list[dict[str, str | int]] | None:
        if rarity == 2:
            return [{"need": 4, "description": sets[0].get("2", "")}]
        elif rarity == 3:
            return [{"need": 3, "description": sets[0].get("2", "")}]
        elif rarity == 4:
            return [{"need": 3, "description": sets[0].get("2", "")}]
        elif rarity == 5:
            return [
                {"need": 2, "description": sets[0].get("2", "")},
                {"need": 4, "description": sets[0].get("4", "")},
            ]
        else:
            return None

    dict_["sets"] = _matrice_set_rework(dict_["rarity"], dict_["set"])
    return dict_


def sort_matrices(matrices: dict[str, "Matrix"]) -> dict[str, "Matrix"]:
    def __sort(matrix: "Matrix") -> tuple[float, float]:
        if matrix.rarity == 5:
            if matrix.banners:
                return -1, -matrix.banners[-1].bannerNumber
            else:
                if matrix.id == "matrix_ssr25" or matrix.id == "matrix_ssr26":
                    return -1, -25.5

                if matrix.id in MATRIX_SORT_ORDER:
                    return -1, MATRIX_SORT_ORDER.index(matrix.id)
                else:
                    return -1, 0

        elif matrix.rarity == 4:
            if matrix.banners:
                return 1, -matrix.banners[-1].bannerNumber
            else:
                if matrix.id in MATRIX_SORT_ORDER:
                    return 1, MATRIX_SORT_ORDER.index(matrix.id)
                else:
                    return 1, 0

        elif matrix.rarity == 3:
            if matrix.banners:
                return 2, -matrix.banners[-1].bannerNumber
            else:
                if matrix.id in MATRIX_SORT_ORDER:
                    return 2, MATRIX_SORT_ORDER.index(matrix.id)
                else:
                    return 2, 0

        elif matrix.rarity == 2:
            if matrix.banners:
                return 3, -matrix.banners[-1].bannerNumber
            else:
                if matrix.id in MATRIX_SORT_ORDER:
                    return 3, MATRIX_SORT_ORDER.index(matrix.id)
                else:
                    return 3, 0

        return 4, 0

    return {matrix.id: matrix for matrix in sorted(list(matrices.values()), key=__sort)}
