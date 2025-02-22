from pydantic import BaseModel


class MiniCategoryBase(BaseModel):
    code: str
    description: str


class ICD10MiniCategoryCreate(MiniCategoryBase):
    pass


class ICD10MiniCategoryResponse(MiniCategoryBase):
    id: int

    class Config:
        from_attributes = True
