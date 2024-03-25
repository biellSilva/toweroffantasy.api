import strawberry
from src.domain.models.base import ModelBase
from src.domain.models.researchs.extras import ResearchMat, ResearchRedo, ResearchReq


class Research(ModelBase):
    name: str
    group: str
    stage: int
    stageIcon: str
    stageInfoIcon: str
    redo: ResearchRedo
    requirements: list[ResearchReq]
    researchMats: list[ResearchMat]
    rewards: list[ResearchMat]


@strawberry.experimental.pydantic.type(model=Research, all_fields=True)
class ResearchType:
    pass
