
from fastapi import APIRouter, Path, Query
from fastapi.responses import ORJSONResponse

from api.enums import WEAPONS, WEAPONS_CN, LANGS, LANGS_CN, VERSIONS
from api.utils import filter_released

from api.infra.entitys import Weapon, EntityBase
from api.infra.repository import WeaponRepo


WEAPON_REPO = WeaponRepo()

router = APIRouter(prefix='/weapons', tags=['Weapons'])
METADATA = {
    'name': 'Weapons',
    'description': ('Weapons obtained from simulacra in Tower of Fantasy \t\n'
                    'CONTAINS CN DATA'),
    }

INCLUDE = {'id', 'name', 'assets', 'category', 'rarity', 'element'}
EXCLUDE = {
    'upgradeMats': True, 
    'weaponAdvancements': {
        '__all__': {
            'multiplier': True
        }
    },
    'weaponAttacks': {
        '__all__': {
            '__all__': 'values'
        }
    }
}


@router.get('/{id}', name='Get weapon', response_model=Weapon)
async def get_weapon(id: WEAPONS = Path(description='Weapon ID'), 
                    #  version: VERSIONS = Query(VERSIONS('global'), description='Game Version'), 
                     lang: LANGS = Query(LANGS('en'), description='Language code'), 
                     include: bool = Query(True, description='Include all data keys')):
    '''
    **Return** \n
        Weapon
    '''

    weapon = await WEAPON_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))

    if include:
        return ORJSONResponse(weapon.model_dump(exclude=EXCLUDE))

    else:
        return ORJSONResponse(weapon.model_dump(include=INCLUDE, exclude=EXCLUDE))


@router.get(path='', name='All Weapons', response_model=list[Weapon])
async def get_all_weapons(# version: VERSIONS = Query(VERSIONS('global'), description='Game Version'), 
                          lang: LANGS = Query(LANGS('en'), description='Language code'), 
                          include: bool = Query(False, description='Include all data keys'), 
                          includeUnreleased: bool = Query(False, description='Include unreleased data')):
    '''
    **Return** \n
        List[Weapon]
    '''

    weapons = await WEAPON_REPO.get_all(lang, version=VERSIONS('global'))

    if not includeUnreleased:
        weapons = filter(filter_released, weapons)

    if include:
        return ORJSONResponse([weapon.model_dump(exclude=EXCLUDE) for weapon in weapons])

    else:
        return ORJSONResponse([weapon.model_dump(include=INCLUDE, exclude=EXCLUDE) for weapon in weapons])
