
from achievements.graphql.achivement import Achievement
from food.graphql.food import Food
from item.graphql.item import Item
from matrices.graphql.matrice import Matrice
from mounts.graphql.mount import Mount
from outfits.graphql.outfit import Outfit
from raritys.graphql.rarity import Raritys
from relics.graphql.relics import Relic
from servants.graphql.servant import SmartServant
from simulacra.graphql.simulacra import Simulacra
from simulacra_v2.graphql.simulacra_v2 import SimulacraV2
from weapons.graphql.weapons import Weapon


__import__ = [
    Achievement,
    Food,
    Item,
    Mount,
    Outfit,
    Raritys,
    Relic,
    SmartServant,
    Simulacra,
    Matrice,
    Weapon,
    SimulacraV2
]