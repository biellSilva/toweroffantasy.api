
from fastapi import APIRouter

from api.enums import FOOD, LANGS


router = APIRouter(prefix="/food", tags=["food"])


@router.get('/{id}')
async def get_food(id: FOOD, lang: LANGS = LANGS('en')):
    pass