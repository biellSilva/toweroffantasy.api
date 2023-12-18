
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from api.enums import WEAPONS, WEAPONS_CN, LANGS, LANGS_CN, VERSIONS

from api.infra.entitys import Weapon, EntityBase
from api.infra.repository import WeaponRepo


WEAPON_REPO = WeaponRepo()

router = APIRouter(prefix='/weapons', tags=['Weapons'])
METADATA = {
    'name': 'Weapons',
    'description': 'Weapons obtained from simulacra in Tower of Fantasy \n\n **CONTAINS CN DATA**',
    }

INCLUDE = {'id', 'name', 'assets', 'category', 'rarity', 'element'}
EXCLUDE = {
    'upgradeMats': True, 
    'weaponAttacks': {
        '__all__': {
            '__all__': 'values'
        }
    }
}


@router.get('/{id}', name='Get weapon', response_model=Weapon)
async def get_weapon(id: WEAPONS | WEAPONS_CN, 
                    #  version: VERSIONS = VERSIONS('global'), 
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
        version (DISABLED):
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

    weapon = await WEAPON_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))

    if include:
        return ORJSONResponse(weapon.model_dump(exclude=EXCLUDE))

    else:
        return ORJSONResponse(weapon.model_dump(include=INCLUDE, exclude=EXCLUDE))


@router.get(path='', name='All Weapons', response_model=list[Weapon])
async def get_all_weapons(# version: VERSIONS = VERSIONS('global'), 
                          lang: LANGS | LANGS_CN = LANGS('en'), 
                          include: bool = False):
    '''
    **Query Params** \n
        version (DISABLED):
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

    weapons = await WEAPON_REPO.get_all(lang, version=VERSIONS('global'))
    if include:
        return ORJSONResponse([weapon.model_dump(exclude=EXCLUDE) for weapon in weapons])

    else:
        return ORJSONResponse([weapon.model_dump(include=INCLUDE, exclude=EXCLUDE) for weapon in weapons])
