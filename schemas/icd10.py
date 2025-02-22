from pydantic import BaseModel, ConfigDict


class ICD10Base(BaseModel):
    code: str
    description: str


class ICD10ChapterCreate(ICD10Base):
    pass


class ICD10ChapterResponse(ICD10Base):
    id: int
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
