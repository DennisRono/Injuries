from pydantic import BaseModel, ConfigDict, UUID4


class CategoryBase(BaseModel):
    code: str
    description: str
    block_id: UUID4


class ICD10CategoryCreate(CategoryBase):
    pass


class ICD10CategoryResponse(CategoryBase):
    id: UUID4
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
