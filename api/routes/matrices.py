
from fastapi import APIRouter

from api.enums import MATRICES, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import MatricesRepo
from api.infra.entitys import EntityBase, Matrix


MATRICE_REPO = MatricesRepo()

router = APIRouter(prefix='/matrices', tags=['Matrices'])
METADATA = {
    'name': 'Matrices',
    'description': ('Matrices are items that can be attached to one of the four weapon slots '
                    '(Emotion, Mind, Belief, and Memory) to provide stat boosts and special effects. \n\n **DOES NOT CONTAINS CN DATA**'),
    }


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
        return PrettyJsonResponse(matrice.model_dump())
    else:
        return PrettyJsonResponse(matrice.model_dump(include={'name', 'id', 'assets', 'rarity'}))



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
    
    matrices = await MATRICE_REPO.get_all(lang=lang, version=VERSIONS('global'))
    if include:
        return PrettyJsonResponse([matrice.model_dump() for matrice in matrices])
    else:
        return PrettyJsonResponse([matrice.model_dump(include={'name', 'id', 'assets', 'rarity'}) for matrice in matrices])
    