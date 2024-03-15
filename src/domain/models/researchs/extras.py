import strawberry
from pydantic import AliasChoices, BaseModel, Field


class ResearchRedo(BaseModel):
    canRedo: bool
    redoAmount: int = Field(validation_alias=AliasChoices("redoAtmt"))


class ResearchReq(BaseModel):
    id: str = Field(validation_alias=AliasChoices("ResearchID"))
    stage: int = Field(validation_alias=AliasChoices("Stage"))


class ResearchMat(BaseModel):
    id: str
    name: str
    description: str
    rarity: int
    icon: str
    type: str
    amount: int = Field(validation_alias=AliasChoices("amt"))


@strawberry.experimental.pydantic.type(model=ResearchRedo, all_fields=True)
class ResearchRedoType:
    pass


@strawberry.experimental.pydantic.type(model=ResearchReq, all_fields=True)
class ResearchReqType:
    pass


@strawberry.experimental.pydantic.type(model=ResearchMat, all_fields=True)
class ResearchMatType:
    pass
