from src._types import LangsEnum
from src.core.router import ApiRouter
from src.exceptions.not_found import MatriceNotFoundError
from src.modules.matrice.model import Suit
from src.modules.matrice.repository import MatriceRepository
from src.modules.matrice.service import MatriceService

router = ApiRouter(prefix="/matrice", tags=["matrice"])

SERVICE = MatriceService(MatriceRepository())


@router.get(
    "/{_id}",
    response_model=Suit,
    exceptions=[MatriceNotFoundError(lang=LangsEnum.EN, id="suit_SSR1")],
)
async def get_matrice(_id: str, lang: LangsEnum = LangsEnum.EN) -> Suit:
    return await SERVICE.get(lang=lang, _id=_id)


@router.get("", response_model=list[Suit])
async def get_all_matrice(lang: LangsEnum = LangsEnum.EN) -> list[Suit]:
    return await SERVICE.get_all(lang=lang)
