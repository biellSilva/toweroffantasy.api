from typing import TYPE_CHECKING

from src.config.sorter import MATRIX_SORT_ORDER
from src.infra.models.matrices import RawMatrix
from src.utils import version_to_float

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


def sort_matrices(
    matrices: dict[str, "Matrix"], china: bool = False
) -> dict[str, "Matrix"]:
    def __sort(matrix: "Matrix") -> tuple[float, float]:
        if matrix.banners:
            return -matrix.rarity, -matrix.banners[-1].bannerNumber

        if matrix.id in MATRIX_SORT_ORDER:
            return -matrix.rarity, MATRIX_SORT_ORDER.index(matrix.id)

        if matrix.id in ("matrix_ssr25", "matrix_ssr26"):
            if china:
                return -matrix.rarity, -2.39
            return -matrix.rarity, -24.9

        if matrix.version and "only" not in matrix.version.lower():
            return -matrix.rarity, -version_to_float(matrix.version)

        return -matrix.rarity, 0

    return {matrix.id: matrix for matrix in sorted(list(matrices.values()), key=__sort)}
