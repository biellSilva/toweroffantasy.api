
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from api.enums import MATRICES, LANGS, VERSIONS
from api.utils import filter_released

from api.infra.repository import MatricesRepo
from api.infra.entitys import EntityBase, Matrix


MATRICE_REPO = MatricesRepo()

router = APIRouter(prefix='/matrices', tags=['Matrices'])
METADATA = {
    'name': 'Matrices',
    'description': ('Matrices are items that can be attached to one of the four weapon slots '
                    '(Emotion, Mind, Belief, and Memory) to provide stat boosts and special effects. \n\n **DOES NOT CONTAINS CN DATA**'),
}

INCLUDE = {'name', 'id', 'assets', 'rarity'}


@router.get('/{id}', name='Get matrix', response_model=Matrix)
async def get_matrice(id: MATRICES, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: Matrix ID

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: Possible languages
        
        include: 
            type: bool
            default: True
            desc: Include all data keys
            
    **Return** \n
        Matrix
    '''
    
    matrice = await MATRICE_REPO.get(EntityBase(id=id), lang, version=VERSIONS('global'))

    if include:
        return ORJSONResponse(matrice.model_dump())
    else:
        return ORJSONResponse(matrice.model_dump(include=INCLUDE))



@router.get('', name='All matrices', response_model=list[Matrix])
async def get_all_matrices(lang: LANGS = LANGS('en'), include: bool = False, released: bool = False):
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
        
        released:
            type: bool
            default: False
            desc: Only released data
            
    **Return** \n
        List[Matrix]
    '''
    
    matrices = await MATRICE_REPO.get_all(lang=lang, version=VERSIONS('global'))

    if released:
        matrices = filter(filter_released, matrices)

    if include:
        return ORJSONResponse([matrice.model_dump() for matrice in matrices])
    else:
        return ORJSONResponse([matrice.model_dump(include=INCLUDE) for matrice in matrices])
    