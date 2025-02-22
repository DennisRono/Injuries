from pydantic import BaseModel


class SubCategoryBase(BaseModel):
    code: str
    description: str


class ICD10SubcategoryCreate(SubCategoryBase):
    pass


class ICD10SubcategoryResponse(SubCategoryBase):
    id: int

    class Config:
        from_attributes = True
