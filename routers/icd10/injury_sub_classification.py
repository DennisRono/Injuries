from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import InjurySubClassification
from schemas.injury_sub_classification import (
    InjurySubClassificationCreate,
    InjurySubClassificationResponse,
)

router = APIRouter()


@router.post(
    "/injury-sub-classification/", response_model=InjurySubClassificationResponse
)
def create_injury_classification(
    block: InjurySubClassificationCreate, db: Session = Depends(get_db)
):
    db_block = InjurySubClassification(**block.dict())
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block


@router.get(
    "/injury-sub-classification/", response_model=List[InjurySubClassificationResponse]
)
def read_injury_classification(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(InjurySubClassification).offset(skip).limit(limit).all()


@router.get(
    "/injury-sub-classification/{id}", response_model=InjurySubClassificationResponse
)
def read_injury_classification_code(id: str, db: Session = Depends(get_db)):
    db_block = (
        db.query(InjurySubClassification)
        .filter(InjurySubClassification.id == id)
        .first()
    )
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    return db_block


@router.put(
    "/injury-sub-classification/{id}", response_model=InjurySubClassificationResponse
)
def update_injury_classification(
    id: str, block: InjurySubClassificationCreate, db: Session = Depends(get_db)
):
    db_block = (
        db.query(InjurySubClassification)
        .filter(InjurySubClassification.id == id)
        .first()
    )
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    for key, value in block.dict().items():
        setattr(db_block, key, value)
    db.commit()
    db.refresh(db_block)
    return db_block


@router.delete(
    "/injury-sub-classification/{id}", response_model=InjurySubClassificationResponse
)
def delete_injury_classification(id: str, db: Session = Depends(get_db)):
    db_block = (
        db.query(InjurySubClassification)
        .filter(InjurySubClassification.id == id)
        .first()
    )
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    db.delete(db_block)
    db.commit()
    return db_block
