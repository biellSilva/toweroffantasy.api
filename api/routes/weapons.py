
from fastapi import APIRouter

from api.enums import WEAPONS, WEAPONS_CN, LANGS, LANGS_CN, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.entitys import Weapon, EntityBase
from api.infra.repository import WeaponRepo


WEAPON_REPO = WeaponRepo()

router = APIRouter(prefix='/weapons', tags=['Weapons'])
METADATA = {
    'name': 'Weapons',
    'description': 'Weapons obtained from simulacra in Tower of Fantasy \n\n **CONTAINS CN DATA**',
    }
INCLUDE = {'name', 'id', 'assets', 'type', 'rarity', 'element'}


@router.get('/{id}', name='Get weapon', response_model=Weapon)
async def get_weapon(id: WEAPONS | WEAPONS_CN, 
                     version: VERSIONS = VERSIONS('global'), 
                     lang: LANGS | LANGS_CN = LANGS('en'), 
                     include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: Weapon ID
            schema: WEAPONS | WEAPONS_CN

    **Query Params** \n
        version:
            type: str
            default: global
            desc: Game version
            schema: VERSIONS
        
        lang:
            type: string
            default: en
            desc: Possible languages
            schema: LANGS | LANGS_CN
    
        include:
            type: bool
            default: False
            desc: Include all data keys

    **Return** \n
        Weapon
    '''

    if version == 'china': # handling cn version
        lang = LANGS_CN('cn')

    weapon = await WEAPON_REPO.get(EntityBase(id=id), lang, version)

    if include:
        return PrettyJsonResponse(weapon.model_dump())

    else:
        return PrettyJsonResponse(weapon.model_dump(include=INCLUDE))


@router.get(path='', name='All Weapons', response_model=list[Weapon])
async def get_all_weapons(version: VERSIONS = VERSIONS('global'), 
                          lang: LANGS | LANGS_CN = LANGS('en'), 
                          include: bool = False):
    '''
    **Query Params** \n
        version:
            type: str
            default: global
            desc: Game version
            schema: VERSIONS
        
        lang:
            type: string
            default: en
            desc: Possible languages
            schema: LANGS | LANGS_CN
    
        include:
            type: bool
            default: False
            desc: Include all data keys
    
    **Return** \n
        List[Weapon]

    '''

    if version == 'china': # handling cn version
        lang = LANGS_CN('cn')

    weapons = await WEAPON_REPO.get_all(lang, version)

    if include:
        return PrettyJsonResponse([weapon.model_dump() for weapon in weapons])

    else:
        return PrettyJsonResponse([weapon.model_dump(include=INCLUDE) for weapon in weapons])
