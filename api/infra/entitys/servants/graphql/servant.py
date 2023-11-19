
import strawberry

@strawberry.type
class ServantAsset:
    petIcon: str
    activatedIcon: str
    itemIcon: str

@strawberry.type
class ServantSkill:
    name: str
    description: str
    icon: str

@strawberry.type
class ServantUpgrade:
    id: str
    xpGain: int

@strawberry.type
class SmartServant:
    id: str
    name: str
    description: str
    rarity: str 
    element: str 
    type: str 
    assets: ServantAsset
    skills: list[ServantSkill]
    upgradeItems: list[ServantUpgrade]
