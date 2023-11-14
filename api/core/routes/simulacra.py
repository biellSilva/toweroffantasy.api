
from fastapi import APIRouter

from api.enums import SIMULACRAS, LANGS

from api.core.exceptions import ItemNotFound
from api.core.response import PrettyJsonResponse

from api.infra.entitys import Simulacra, EntityBase
from api.infra.repository import SimulacraRepo


router = APIRouter(prefix='/simulacra', tags=['simulacra'])


SIMU_REPO = SimulacraRepo()


@router.get('/{id}', name='Get simulacra', response_model=Simulacra)
async def get_simulacra(id: SIMULACRAS, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: string
            required: True
            desc: imitation_id

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
        Simulacra
    '''
    
    if simulacra := await SIMU_REPO.get(EntityBase(id=id), lang):
        if include:
            return PrettyJsonResponse(simulacra.model_dump())
        else:
            return PrettyJsonResponse(simulacra.model_dump(include={'id', 'name', 'assets', 'weapon_id'}))
    
    else:
        raise ItemNotFound(detail={'error': f'{id} not found in {lang}'})

@router.get('', name='All simulacras', response_model=list[Simulacra])
async def get_all_simulacra(lang: LANGS = LANGS('en'), include: bool = False):
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
        List[Simulacra]
    '''
    
    if simulacras := await SIMU_REPO.get_all(lang):
        if include:
            return PrettyJsonResponse([simulacra.model_dump() for simulacra in simulacras])
        else:
            return PrettyJsonResponse([simulacra.model_dump(include={'id', 'name', 'assets', 'weapon_id'}) for simulacra in simulacras])
    
    else:
        raise ItemNotFound(detail={'error': f'{lang} not found'})