from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import InjuryClassification
from schemas.injury_classification import (
    InjuryClassificationCreate,
    InjuryClassificationResponse,
)

router = APIRouter()


@router.post("/injury-classification/", response_model=InjuryClassificationResponse)
def create_injury_classification(
    block: InjuryClassificationCreate, db: Session = Depends(get_db)
):
    db_block = InjuryClassification(**block.dict())
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block


@router.get(
    "/injury-classification/", response_model=List[InjuryClassificationResponse]
)
def read_injury_classification(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(InjuryClassification).offset(skip).limit(limit).all()


@router.get("/injury-classification/{id}", response_model=InjuryClassificationResponse)
def read_injury_classification_code(id: str, db: Session = Depends(get_db)):
    db_block = (
        db.query(InjuryClassification).filter(InjuryClassification.id == id).first()
    )
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    return db_block


@router.put("/injury-classification/{id}", response_model=InjuryClassificationResponse)
def update_injury_classification(
    id: str, block: InjuryClassificationCreate, db: Session = Depends(get_db)
):
    db_block = (
        db.query(InjuryClassification).filter(InjuryClassification.id == id).first()
    )
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    for key, value in block.dict().items():
        setattr(db_block, key, value)
    db.commit()
    db.refresh(db_block)
    return db_block


@router.delete(
    "/injury-classification/{id}", response_model=InjuryClassificationResponse
)
def delete_injury_classification(id: str, db: Session = Depends(get_db)):
    db_block = (
        db.query(InjuryClassification).filter(InjuryClassification.id == id).first()
    )
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    db.delete(db_block)
    db.commit()
    return db_block
