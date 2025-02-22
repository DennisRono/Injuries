from pydantic import BaseModel, ConfigDict


class ClaimBase(BaseModel):
    patient_id: int
    injury_id: int
    status: str
    compensation_amount: float


class ClaimCreate(ClaimBase):
    pass


class ClaimResponse(ClaimBase):
    id: int
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
