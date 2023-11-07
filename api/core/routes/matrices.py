
from fastapi import APIRouter

from api.enums import MATRICES, LANGS

from api.core.exceptions import ItemNotFound
from api.core.response import PrettyJsonResponse

from api.infra.repository import MatriceRepo
from api.infra.entitys import EntityBase, Matrice



router = APIRouter(prefix='/matrices', tags=['matrices'])

MATRICE_REPO = MatriceRepo()

@router.get('/{id}', response_model=Matrice)
async def get_matrice(id: MATRICES, lang: LANGS = LANGS('en')):
    '''
    RETURNS \n
        Matrice
    '''
    
    if matrice := await MATRICE_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(matrice.model_dump(exclude_none=True))

    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})

@router.get('', response_model=dict[str, Matrice])
async def get_all_matrices(lang: LANGS = LANGS('en')):
    '''
    RETURNS \n
        Dict[Matrice.id: Matrice] 
    '''
    
    if matrices := await MATRICE_REPO.get_all(lang):
        return PrettyJsonResponse({matrice.id: matrice.model_dump(exclude_none=True) 
                                   for matrice in matrices})
    
    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})