
from fastapi import APIRouter

from api.enums import RELICS, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import RelicRepo
from api.infra.entitys import Relic, EntityBase


RELIC_REPO = RelicRepo()

router = APIRouter(prefix='/relics', tags=['Relics'])
METADATA = {
    'name': 'Relics',
    'description': 'Relics are tools that aid the player in exploration or combat \n\n **DOES NOT CONTAINS CN DATA**',
    }


@router.get('/{id}', name='Get relic', response_model=Relic)
async def get_relic(id: RELICS, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: relic_id
            
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
        Relic
    '''

    relic = await RELIC_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(relic.model_dump())
    else:
        return PrettyJsonResponse(relic.model_dump(include={'name', 'id', 'icon', 'rarity'}))



@router.get('', name='All relics', response_model=list[Relic])
async def get_all_relics(lang: LANGS = LANGS('en'), include: bool = False):
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
        List[Relic]
    '''

    relics = await RELIC_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([relic.model_dump() for relic in relics])
    else:
        return PrettyJsonResponse([relic.model_dump(include={'name', 'id', 'icon', 'rarity'}) for relic in relics])
