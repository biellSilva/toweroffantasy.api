

from fastapi import APIRouter
from api.core.exceptions import ItemNotFound

from api.enums import MATRICES, LANGS
from api.infra.repository import MatriceRepo
from api.infra.entitys import EntityBase


router = APIRouter(prefix='/matrices', tags=['matrices'])

MATRICE_REPO = MatriceRepo()

@router.get('/{id}', response_model_exclude_none=True)
async def get_matrice(id: MATRICES, lang: LANGS = LANGS('en')):
    ''' Get matrice based on ID '''
    
    if matrice := await MATRICE_REPO.get(EntityBase(id=id), lang):
        return matrice

    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})