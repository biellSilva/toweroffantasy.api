
from typing import Any
from src.domain.usecases.relics.get_all import GetAllRelicsParams, GetAllRelicsResult, IGetAllRelicsUseCase


class GetAllRelicsUseCase(IGetAllRelicsUseCase):
    def __init__(self, repository: GetAllRepository) -> None:
        self.repository = repository

        
    async def execute(self, params: GetAllRelicsParams) -> GetAllRelicsResult:
        ...


