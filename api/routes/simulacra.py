
from fastapi import APIRouter, Path, Query
from fastapi.responses import ORJSONResponse

from api.enums import SIMULACRA, SIMULACRA_CN, LANGS, LANGS_CN, VERSIONS
from api.utils import filter_released

from api.infra.entitys import Simulacra, EntityBase
from api.infra.repository import SimulacraRepo


SIMU_REPO = SimulacraRepo()

router = APIRouter(prefix='/simulacra', tags=['Simulacra'])
METADATA = {
    'name': 'Simulacra',
    'description': ('Simulacra are the player\'s representation of the characters found in Tower of Fantasy \t\n'
                    'CONTAINS CN DATA'),
    }

INCLUDE = {'id', 'name', 'assetsA0', 'weaponId', 'matrixId', 'rarity'}


@router.get('/{id}', name='Get simulacrum', response_model=Simulacra)
async def get_simulacrum(id: SIMULACRA = Path(description='Imitation/Simulacrum ID'), 
                        #  version: VERSIONS = Query(VERSIONS('global'), description='Game Version'),
                         lang: LANGS = Query(LANGS('en'), description='Language code'), 
                         include: bool = Query(True, description='Include all data keys')
):
    '''
    **Return** \n
        Simulacra
    '''
    
    simulacra = await SIMU_REPO.get(EntityBase(id=id), lang, version=VERSIONS('global'))

    if include:
        return ORJSONResponse(simulacra.custom_model_dump())
    else:
        return ORJSONResponse(simulacra.custom_model_dump(include=INCLUDE))
    


@router.get('', name='All simulacra', response_model=list[Simulacra])
async def get_all_simulacra(version: VERSIONS = Query(VERSIONS('global'), description='Game Version'), 
                            lang: LANGS = Query(LANGS('en'), description='Language code'), 
                            include: bool = Query(False, description='Include all data keys'), 
                            includeUnreleased: bool = Query(False, description='Include unreleased data')):
    '''
    **Return** \n
        List[Simulacra]
    '''
    
    simulacra = await SIMU_REPO.get_all(lang=lang, version=version)

    if not includeUnreleased:
        simulacra = filter(filter_released, simulacra)

    if include:
        return ORJSONResponse([simulacrum.model_dump() for simulacrum in simulacra])
    else:
        return ORJSONResponse([simulacrum.model_dump(include=INCLUDE) for simulacrum in simulacra])
    