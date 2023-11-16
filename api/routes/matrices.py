
from fastapi import APIRouter

from api.enums import MATRICES, LANGS

from api.core.exceptions import ItemNotFound
from api.core.response import PrettyJsonResponse

from api.infra.repository import MatricesRepo
from api.infra.entitys import EntityBase, Matrix



router = APIRouter(prefix='/matrices', tags=['Matrices'])

MATRICE_REPO = MatricesRepo()

@router.get('/{id}', name='Get matrix', response_model=Matrix)
async def get_matrice(id: MATRICES, lang: LANGS = LANGS('en'), include: bool = True):
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
        
        include: 
            type: bool
            default: True
            desc: Include all data keys
            
    **Return** \n
        Matrix
    '''
    
    if matrice := await MATRICE_REPO.get(EntityBase(id=id), lang):
        if include:
            return PrettyJsonResponse(matrice.model_dump())
        else:
            return PrettyJsonResponse(matrice.model_dump(include={'name', 'id', 'icon'}))

    else:
        raise ItemNotFound(detail={'error': f'{id} not found in {lang}'})

@router.get('', name='All matrices', response_model=list[Matrix])
async def get_all_matrices(lang: LANGS = LANGS('en'), include: bool = False):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
        
        include:
            type: bool
            default: False
            desc: Include all data keys
            
    **Return** \n
        List[Matrix]
    '''
    
    if matrices := await MATRICE_REPO.get_all(lang):
        if include:
            return PrettyJsonResponse([matrice.model_dump() for matrice in matrices])
        else:
            return PrettyJsonResponse([matrice.model_dump(include={'name', 'id', 'icon', 'rarity'}) for matrice in matrices])
    
    else:
        raise ItemNotFound(detail={'error': f'{lang} not found'})