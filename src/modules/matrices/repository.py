from src.modules.base.json_repository import JsonRepository


class MatriceRepository(JsonRepository):
    def __init__(self) -> None:
        super().__init__(name="matrices")
