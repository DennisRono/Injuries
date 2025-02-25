from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import Injury
from schemas.injury import (
    InjuryCreate,
    InjuryResponse,
)

router = APIRouter()


@router.post("/injury/", response_model=InjuryResponse)
def create_injury_classification(block: InjuryCreate, db: Session = Depends(get_db)):
    db_block = Injury(**block.dict())
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block


@router.get("/injury/", response_model=List[InjuryResponse])
def read_injury_classification(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(Injury).offset(skip).limit(limit).all()


@router.get("/injury/{id}", response_model=InjuryResponse)
def read_injury_classification_code(id: str, db: Session = Depends(get_db)):
    db_block = db.query(Injury).filter(Injury.id == id).first()
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    return db_block


@router.put("/injury/{id}", response_model=InjuryResponse)
def update_injury_classification(
    id: str, block: InjuryCreate, db: Session = Depends(get_db)
):
    db_block = db.query(Injury).filter(Injury.id == id).first()
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    for key, value in block.dict().items():
        setattr(db_block, key, value)
    db.commit()
    db.refresh(db_block)
    return db_block


@router.delete("/injury/{id}", response_model=InjuryResponse)
def delete_injury_classification(id: str, db: Session = Depends(get_db)):
    db_block = db.query(Injury).filter(Injury.id == id).first()
    if db_block is None:
        raise HTTPException(status_code=404, detail="injury classification not found")
    db.delete(db_block)
    db.commit()
    return db_block
