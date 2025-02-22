from pydantic import BaseModel


class ClaimBase(BaseModel):
    patient_id: int
    injury_id: int
    status: str
    compensation_amount: float


class ClaimCreate(ClaimBase):
    pass


class ClaimResponse(ClaimBase):
    id: int

    class Config:
        from_attributes = True
