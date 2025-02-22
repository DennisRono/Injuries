from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import ICD10
from schemas.icd10 import ICD10Create, ICD10Response

router = APIRouter()


@router.post("/icd10/", response_model=ICD10Response)
def create_icd10(icd10: ICD10Create, db: Session = Depends(get_db)):
    db_icd10 = ICD10(**icd10.dict())
    db.add(db_icd10)
    db.commit()
    db.refresh(db_icd10)
    return db_icd10


@router.get("/icd10/", response_model=List[ICD10Response])
def read_icd10_codes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(ICD10).offset(skip).limit(limit).all()


@router.get("/icd10/{code}", response_model=ICD10Response)
def read_icd10(code: str, db: Session = Depends(get_db)):
    db_icd10 = db.query(ICD10).filter(ICD10.code == code).first()
    if db_icd10 is None:
        raise HTTPException(status_code=404, detail="ICD-10 code not found")
    return db_icd10
