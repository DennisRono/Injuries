from pydantic import BaseModel, ConfigDict, UUID4


class SubCategoryBase(BaseModel):
    code: str
    description: str
    category_id: UUID4


class ICD10SubcategoryCreate(SubCategoryBase):
    pass


class ICD10SubcategoryResponse(SubCategoryBase):
    id: UUID4
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
