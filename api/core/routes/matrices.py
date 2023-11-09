
from fastapi import APIRouter

from api.enums import MATRICES, LANGS

from api.core.exceptions import ItemNotFound
from api.core.response import PrettyJsonResponse

from api.infra.repository import MatriceRepo
from api.infra.entitys import EntityBase, Matrice



router = APIRouter(prefix='/matrice', tags=['matrice'])

MATRICE_REPO = MatriceRepo()

@router.get('/{id}', name='Get matrice', response_model=Matrice)
async def get_matrice(id: MATRICES, lang: LANGS = LANGS('en')):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: matrice_id

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
    **Return** \n
        Matrice
    '''
    
    if matrice := await MATRICE_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(matrice.model_dump())

    else:
        raise ItemNotFound(detail={'error': f'{id} not found in {lang}'})

@router.get('', name='All matrices', response_model=list[Matrice])
async def get_all_matrices(lang: LANGS = LANGS('en')):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
    **Return** \n
        List[Matrice]
    '''
    
    if matrices := await MATRICE_REPO.get_all(lang):
        return PrettyJsonResponse([matrice.model_dump() for matrice in matrices])
    
    else:
        raise ItemNotFound(detail={'error': f'{lang} not found'})