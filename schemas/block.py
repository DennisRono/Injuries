from pydantic import BaseModel, ConfigDict, UUID4


class BlockBase(BaseModel):
    code: str
    description: str
    chapter_id: UUID4


class ICD10BlockCreate(BlockBase):
    pass


class ICD10BlockResponse(BlockBase):
    id: UUID4
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
