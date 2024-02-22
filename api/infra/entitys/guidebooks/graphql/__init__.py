import strawberry


@strawberry.type
class GuideBookItem:
    title: str
    icon: str
    description: str


@strawberry.type
class Guidebook:
    id: str
    name: str
    icon: str
    items: list[GuideBookItem]
    menuId: str
    menuType: str
