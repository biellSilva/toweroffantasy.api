
import re

from typing import TYPE_CHECKING, TypeVar

from api.enums import LANGS

if TYPE_CHECKING:
    from api.infra.entitys import Simulacra, Weapon, Matrix, Simulacra_v2


T = TypeVar('T')


# Sort order for items that do not have a banner. 
# Useful to keep a consistent order of data across languages, 
# because sorting by name may result in a different order of data based on the language.

SIMULACRA_SORT_ORDER = [
    "imitation_11",     # Cocoritter
    "imitation_13",     # Crow
    "imitation_6",      # Huma
    "imitation_9",      # KING
    "imitation_3",      # Meryl
    "imitation_33",     # Samir
    "imitation_5",      # Shiro
    "imitation_8",      # Tsubasa
    "imitation_7",      # Zero
    "imitation_1",      # Bai Ling
    "imitation_16",     # Echo
    "imitation_4",      # Ene
    "imitation_2",      # Hilda
    "imitation_15",     # Pepper
    "imitation_14",
]

WEAPON_SORT_ORDER = [
    "stave_ice",
    "digger_thunder",
    "shieldaxe_fire",
    "sickle_fire",
    "bigsword_ice",
    # null,             # Molinia
    "dgun_thunder",
    "darts_physic",
    "bow_ice",
    "cube_fire",
    "bow_physic",
    "spear_thunder",
    "hammer_ice",
    "cannon_ice",
    "stave_thunder",
    "digger_physic",    # Combat Blade
    "bow_fire",         # Composite Bow
    "sword_thunder",    # EM Blade
    "spear_ice"         # Frosted Spear
]

MATRIX_SORT_ORDER = [
    "matrix_ssr3",
    "matrix_ssr11",
    "matrix_ssr10",
    "matrix_ssr4",
    "matrix_ssr1",
    # null,             # Molinia
    "matrix_ssr9",
    "matrix_ssr7",
    "matrix_ssr2",
    "matrix_ssr8",
    "matrix_sr2",       # Apophis
    "matrix_sr9",       # Bai Ling
    "matrix_sr5",       # Barbarossa
    "matrix_sr12",      # Echo
    "matrix_sr8",       # Ene
    "matrix_sr3",       # Frost Bot
    "matrix_sr7",       # Hilda
    "matrix_sr6",       # Pepper
    "matrix_sr4",       # Sobek
    "matrix_sr1",       # Robarg
    "matrix_r6",        # Attack Analyzer
    "matrix_r1",        # Explosive Core
    "matrix_r2",        # Hauler
    "matrix_r4",        # Provocateurs
    "matrix_r7",        # Purge Pact
    "matrix_r3",        # Standard Guard
    "matrix_n2",        # Overheat
    "matrix_n1",        # Wandering Aberrant
]



def bold_numbers(text: str):
    text_a = re.sub(r'\<[a-zA-Z]+\>(\D)+\<\/\>', 
                  lambda x: x.group(0).replace("<shuzhi>", "**").replace("<red>", "**").replace("<blue>", "**").replace("<green>", "**").replace("<ComLblGreen>", "**").replace("</>", "**")
                            if text[x.span(0)[0]-1] != '*' else x.group(0), 
                  text, flags=re.UNICODE)
    
    text_b = re.sub(r'\+?\{?\d+(\.?\,?\d+)?\}?%?', 
                  lambda x: f'**{x.group(0)}**' if text_a[x.span(0)[0]-1] != '*' else x.group(0), 
                  text_a.replace("<shuzhi>", "").replace("<red>", "").replace("<blue>", "").replace("<green>", "").replace("</>", ""), 
                  flags=re.UNICODE)
    
    return text_b

def replace_cv(text: str):
    if not text or text == '':
        return None
    return text.replace('CV : ', '')

def replace_icon(text: str):
    if '/Game/Resources/' in text:
        return text.replace('/Game/Resources', '/assets')
    else:
        return text

def localized_asset(text: str, lang: LANGS):
    return f'/assets/L10N/{lang}/Resources/{text.replace("/Game/Resources/", "")}'

def put_imitation_icon(text: str):
    if '/assets' in text:
        return text
    return f'/assets/UI/huanxing/lihui/{text}'

def check_string(text: str):
    if text.lower() == 'none':
        return None
    return text

def replace_rarity_asset(text: str):
    if text.lower() == 'none':
        return None
    if '/Game/Resources/' in text:
        return text.replace('/Game/Resources', '/assets')
    else:
        return text

def classifier(number: float):
    if number >= 15:
        return 'SS'
    elif number >= 10.01:
        return 'S'
    elif number >= 8:
        return 'A'
    elif number >= 4:
        return 'B'
    else:
        return 'C'
    
def matrice_set_rework(rarity: str, sets: list[dict[str, str]]):
    if rarity == 'N':
        return [{'need': 4, 'description': sets[0].get('2', '')}]
    elif rarity == 'R':
        return [{'need': 3, 'description': sets[0].get('2', '')}]
    elif rarity == 'SR':
        return [{'need': 3, 'description': sets[0].get('2', '')}]
    elif rarity == 'SSR':
        return [{'need': 2, 'description': sets[0].get('2', '')}, 
                {'need': 4, 'description': sets[0].get('4', '')}]
    else:
        return None

def trait_rework(trait: dict[str, dict[str, str]]):
    return [value for key, value in trait.items() if not key == 'id']

def voice_actors_rework(va: list[dict[str, str]]):
    return {key.lower(): value for i in va for key, value in i.items()}

def voice_actor_string_rework(actor: str):
    return actor.removeprefix(' ')

def classify_rework(value: float):
    return {'tier': classifier(value), 'value': value}

def material_rework(mats: dict[str, int]):
    return [{'id': key.lower(), 'need': value} for key, value in mats.items()]

def pet_material_rework(mats: dict[str, int]):
    return [{'id': key.lower(), 'xpGain': value} for key, value in mats.items()]

def relic_advanc_rework(advanc: list[dict[str, str]]):
    return [value for i in advanc for key, value in i.items() if not key == 'id']


def sort_simulacra(simulacrum: 'Simulacra') -> tuple[int, int]:
    if simulacrum.rarity == 'SSR':
        if simulacrum.banners:
            return -1, -simulacrum.banners[-1].bannerNumber
        else:
            if simulacrum.id in SIMULACRA_SORT_ORDER:
                return -1, SIMULACRA_SORT_ORDER.index(simulacrum.id)
            else:
                return -1, 0
        
    elif simulacrum.rarity == 'SR':
        if simulacrum.banners:
            return 1, -simulacrum.banners[-1].bannerNumber
        else:
            if simulacrum.id in SIMULACRA_SORT_ORDER:
                return 1, SIMULACRA_SORT_ORDER.index(simulacrum.id)
            else:
                return 1, 0
        
    return 2, 0

def sort_weapons(weapon: 'Weapon') -> tuple[int, int]:
    if weapon.rarity == 'SSR':
        if weapon.banners:
            return -1, -weapon.banners[-1].bannerNumber
        else:
            if weapon.id in WEAPON_SORT_ORDER:
                return -1, WEAPON_SORT_ORDER.index(weapon.id)
            else:
                return -1, 0
    
    elif weapon.rarity == 'SR':
        if weapon.banners:
            return 1, -weapon.banners[-1].bannerNumber
        else:
            if weapon.id in WEAPON_SORT_ORDER:
                return 1, WEAPON_SORT_ORDER.index(weapon.id)
            else:
                return 1, 0
    
    elif weapon.rarity == 'R':
        if weapon.banners:
            return 2, -weapon.banners[-1].bannerNumber
        else:
            if weapon.id in WEAPON_SORT_ORDER:
                return 2, WEAPON_SORT_ORDER.index(weapon.id)
            else:
                return 2, 0
            
    return 3, 0


def sort_matrices(matrice: 'Matrix') -> tuple[int, float]:
    if matrice.rarity == 'SSR':
        if matrice.banners:
            return -1, -matrice.banners[-1].bannerNumber
        else:
            if matrice.id == 'matrix_ssr25' or matrice.id == 'matrix_ssr26':
                return -1, -25.5
        
            if matrice.id in MATRIX_SORT_ORDER:
                return -1, MATRIX_SORT_ORDER.index(matrice.id)
            else:
                return -1, 0
    
    elif matrice.rarity == 'SR':
        if matrice.banners:
            return 1, -matrice.banners[-1].bannerNumber
        else:
            if matrice.id in MATRIX_SORT_ORDER:
                return 1, MATRIX_SORT_ORDER.index(matrice.id)
            else:
                return 1, 0
    
    elif matrice.rarity == 'R':
        if matrice.banners:
            return 2, -matrice.banners[-1].bannerNumber
        else:
            if matrice.id in MATRIX_SORT_ORDER:
                return 2, MATRIX_SORT_ORDER.index(matrice.id)
            else:
                return 2, 0

    elif matrice.rarity == 'N':
        if matrice.banners:
            return 3, -matrice.banners[-1].bannerNumber
        else:
            if matrice.id in MATRIX_SORT_ORDER:
                return 3, MATRIX_SORT_ORDER.index(matrice.id)
            else:
                return 3, 0
    
    return 4, 0


def place_numbers(weapon: 'Weapon'):
    for attack in weapon.weaponAttacks.normals:
        if attack.description and r'{0}' in attack.description:
            if not attack.values:
                print(attack.id, [i[-1] for i in attack.values])
                continue

            new_desc = attack.description.format(*[i[-1] for i in attack.values])
            attack.description = new_desc
    
    for attack in weapon.weaponAttacks.dodge:
        if attack.description and r'{0}' in attack.description:
            if not attack.values:
                print(attack.id, [i[-1] for i in attack.values])
                continue

            new_desc = attack.description.format(*[i[-1] for i in attack.values])
            attack.description = new_desc

    for attack in weapon.weaponAttacks.skill:
        if attack.description and r'{0}' in attack.description:
            if not attack.values:
                print(attack.id, [i[-1] for i in attack.values])
                continue

            new_desc = attack.description.format(*[i[-1] for i in attack.values])
            attack.description = new_desc

    for attack in weapon.weaponAttacks.discharge:
        if attack.description and r'{0}' in attack.description:
            if not attack.values:
                print(attack.id, [i[-1] for i in attack.values])
                continue

            new_desc = attack.description.format(*[i[-1] for i in attack.values])
            attack.description = new_desc

    return weapon

def place_numbers_v2(simulacra: 'Simulacra_v2'):
    if simulacra.weapon:
        for attack in simulacra.weapon.weaponAttacks.normals:
            if attack.description and r'{0}' in attack.description:
                if not attack.values:
                    print(attack.id, [i[-1] for i in attack.values])
                    continue

                new_desc = attack.description.format(*[i[-1] for i in attack.values])
                attack.description = new_desc
        
        for attack in simulacra.weapon.weaponAttacks.dodge:
            if attack.description and r'{0}' in attack.description:
                if not attack.values:
                    print(attack.id, [i[-1] for i in attack.values])
                    continue

                new_desc = attack.description.format(*[i[-1] for i in attack.values])
                attack.description = new_desc

        for attack in simulacra.weapon.weaponAttacks.skill:
            if attack.description and r'{0}' in attack.description:
                if not attack.values:
                    print(attack.id, [i[-1] for i in attack.values])
                    continue

                new_desc = attack.description.format(*[i[-1] for i in attack.values])
                attack.description = new_desc

        for attack in simulacra.weapon.weaponAttacks.discharge:
            if attack.description and r'{0}' in attack.description:
                if not attack.values:
                    print(attack.id, [i[-1] for i in attack.values])
                    continue

                new_desc = attack.description.format(*[i[-1] for i in attack.values])
                attack.description = new_desc
    
    return simulacra


def paginator(items: list[T], page: int = 0, chunk: int = 10) -> tuple[list[T], int]:
    return items[page*chunk : page*chunk+chunk], len(items) // chunk if len(items) % chunk == 0 else len(items) // chunk + 1
