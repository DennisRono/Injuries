from pydantic import BaseModel


class ICD10Base(BaseModel):
    code: str
    description: str


class ICD10ChapterCreate(ICD10Base):
    pass


class ICD10ChapterResponse(ICD10Base):
    id: int

    class Config:
        from_attributes = True
