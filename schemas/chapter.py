from pydantic import BaseModel


class ChapterBase(BaseModel):
    code: str
    description: str


class ICD10ChapterCreate(ChapterBase):
    pass


class ICD10ChapterResponse(ChapterBase):
    id: int

    class Config:
        from_attributes = True
