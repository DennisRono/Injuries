from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.patient import Patient
from schemas.patient import PatientCreate, PatientResponse

router = APIRouter()


@router.post("/patients/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


@router.get("/patients/", response_model=List[PatientResponse])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Patient).offset(skip).limit(limit).all()


@router.get("/patients/{patient_id}", response_model=PatientResponse)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient
