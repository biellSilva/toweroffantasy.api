
from fastapi import APIRouter

from api.enums import SIMULACRAS, LANGS

from api.core.exceptions import ItemNotFound
from api.core.response import PrettyJsonResponse

from api.infra.entitys import Simulacra, EntityBase
from api.infra.repository import SimulacraRepo


router = APIRouter(prefix='/simulacra', tags=['simulacra'])


SIMU_REPO = SimulacraRepo()


@router.get('/{id}', response_model=Simulacra)
async def get_simulacra(id: SIMULACRAS, lang: LANGS = LANGS('en')):
    '''
    return \n
        Simulacra
    '''
    
    if simulacra := await SIMU_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(simulacra.model_dump())
    
    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})

@router.get('', response_model=dict[str, Simulacra])
async def get_all_simulacra(lang: LANGS = LANGS('en')):
    '''
    return \n
        Simulacra
    '''
    
    if simulacras := await SIMU_REPO.get_all(lang):
        return PrettyJsonResponse({simulacra.id: simulacra.model_dump() 
                                   for simulacra in simulacras})
    
    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})