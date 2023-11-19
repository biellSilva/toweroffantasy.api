
from pathlib import Path
from json import loads

from api.infra.entitys.banners import Banner


GLOBAL_ASSETS = 'https://raw.githubusercontent.com/FortOfFans/ToF.github.io/main'
CN_ASSETS = 'https://raw.githubusercontent.com/Silyky/Icon_CN/main'


GB_BANNERS: list[Banner] = [Banner(**data) for data in loads(Path(f'api/infra/database/global/banners_global.json').read_bytes())]


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
    "matrix_sr9",
    "matrix_sr12",
    "matrix_sr8",
    "matrix_sr7",
    "matrix_sr6",
    "matrix_r6",        # Attack Analyzer
    "matrix_r1",        # Explosive Core
    "matrix_r2",        # Hauler
    "matrix_r4",        # Provocateurs
    "matrix_r7",        # Purge Pact
    "matrix_r3",        # Standard Guard
    "matrix_n2",        # Overheat
    "matrix_n1",        # Wandering Aberrant
]