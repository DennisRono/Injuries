from pydantic import BaseModel


class CategoryBase(BaseModel):
    code: str
    description: str


class ICD10CategoryCreate(CategoryBase):
    pass


class ICD10CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True
