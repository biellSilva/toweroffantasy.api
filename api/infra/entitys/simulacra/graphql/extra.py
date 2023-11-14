
import strawberry


@strawberry.type
class VoiceActors:
    chinese:str | None 
    japanese: str | None 
    english: str | None 
    korean: str | None 
    portuguese: str | None 


@strawberry.type
class Awakening:
    name: str
    description: str


@strawberry.type
class Assets:
    avatar: str | None 
    artwork: str | None 
    lotteryCard: str | None 
    lotteryDrawing: str | None 


@strawberry.type
class Banner:
    bannerNo: int
    start: str
    end: str
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool
    