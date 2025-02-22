from pydantic import BaseModel, ConfigDict


class PatientBase(BaseModel):
    name: str
    date_of_birth: str


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )
