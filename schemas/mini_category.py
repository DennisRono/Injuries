from pydantic import BaseModel, UUID4, ConfigDict


class MiniCategoryBase(BaseModel):
    code: str
    description: str
    subcategory_id: UUID4


class ICD10MiniCategoryCreate(MiniCategoryBase):
    pass


class ICD10MiniCategoryResponse(MiniCategoryBase):
    id: UUID4
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
