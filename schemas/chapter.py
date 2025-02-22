from pydantic import BaseModel, UUID4, ConfigDict


class ChapterBase(BaseModel):
    range_code: str
    description: str


class ICD10ChapterCreate(ChapterBase):
    pass


class ICD10ChapterResponse(ChapterBase):
    id: UUID4
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
