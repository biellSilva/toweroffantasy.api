
from fastapi import APIRouter, Query, Path
from fastapi.responses import ORJSONResponse

from api.enums import SIMULACRA, LANGS, VERSIONS
from api.utils import paginator

from api.infra.repository import SimulacraV2Repo
from api.infra.entitys import EntityBase, Simulacra_v2


SIMULACRA_REPO = SimulacraV2Repo()

router = APIRouter(prefix='/simulacra-v2', tags=['Simulacra v2'])
METADATA = {
    'name': 'Simulacra v2',
    'description': 'Simulacra v2 is the same as /simulacra, except it contains Weapons and Matrices if possible \n\n **DOES NOT CONTAINS CN DATA**',
}
EXCLUDE = {'weapon': {'weaponAttacks': {'__all__': {'__all__': 'values'}}}}
INCLUDE = {
    'id': True, 
    'name': True, 
    'assetsA0': True, 
    'weaponId': True, 
    'matrixId': True, 
    'rarity': True, 
    'weapon': {
        'id': True, 
        'name': True, 
        'element': True, 
        'category': True,
        'assets': True
    },
    'matrix': {
        'name': True, 
        'id': True, 
        'assets': True, 
        'rarity': True,
        'assets': True,
    }
}


@router.get('/{id}', name='Get Simulacrum', response_model=Simulacra_v2)
async def get_simulacrum(id: SIMULACRA = Path(description='Imitation/Simulacrum Id'), 
                         lang: LANGS = Query(LANGS('en'), description='Possible languages'),
                         include: bool = Query(True, description='Include all data keys')):
    '''
    **Path Param** \n
        id: 
            type: string
            required: True
            desc: Imitation/Simulacra ID

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
        Simulacra_v2
    '''
    
    simulacrum = await SIMULACRA_REPO.get(EntityBase(id=id), lang, version=VERSIONS('global'))
    if include:
        return ORJSONResponse(simulacrum.model_dump(exclude=EXCLUDE))
    
    else:
        return ORJSONResponse(simulacrum.model_dump(include=INCLUDE, exclude=EXCLUDE))


@router.get('', name='All Simulacra', response_model=list[Simulacra_v2])
async def get_simulacra(lang: LANGS = Query(LANGS('en'), description='Possible languages'),
                        include: bool = Query(False, description='Include all data keys'), 
                        page: int | None = Query(None, description='Page to return'),
                        chunk: int | None = Query(None, description='How many items per page')):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: Possible languages
        
        page:
            type: int
            default: None
            desc: Page to return
        
        chunk:
            type: int
            default: None | 10 *if page is used*
            desc: How many items per page
            
    **Return** \n
        List[Simulacra_v2]
    '''
    
    simulacra = await SIMULACRA_REPO.get_all(lang, version=VERSIONS('global'))

    if page:
        if chunk:
            items, pages = paginator(items=simulacra, page=page, chunk=chunk)
        else:
            items, pages = paginator(items=simulacra, page=page)

        if include:
            return ORJSONResponse([simulacrum.model_dump(exclude=EXCLUDE) for simulacrum in items],
                                  headers={'pages': str(pages)})
        else:
            return ORJSONResponse([simulacrum.model_dump(include=INCLUDE, exclude=EXCLUDE) for simulacrum in items],
                                  headers={'pages': str(pages)})
    else:
        if include:
            return ORJSONResponse([simulacrum.model_dump(exclude=EXCLUDE) for simulacrum in simulacra])
        else:
            return ORJSONResponse([simulacrum.model_dump(include=INCLUDE, exclude=EXCLUDE) for simulacrum in simulacra])