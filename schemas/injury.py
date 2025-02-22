from pydantic import BaseModel, ConfigDict, UUID4

from schemas.mini_category import ICD10MiniCategoryResponse


class InjuryBase(BaseModel):
    ais_code: str
    description: str


class InjuryCreate(InjuryBase):
    pass


class InjuryResponse(InjuryBase):
    id: UUID4
    icd10_mini_category: ICD10MiniCategoryResponse
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
