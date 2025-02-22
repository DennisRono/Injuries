from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import ICD10Block
from schemas.block import ICD10BlockCreate, ICD10BlockResponse

router = APIRouter()


@router.post("/blocks/", response_model=ICD10BlockResponse)
def create_icd10_block(block: ICD10BlockCreate, db: Session = Depends(get_db)):
    db_block = ICD10Block(**block.dict())
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block


@router.get("/blocks/", response_model=List[ICD10BlockResponse])
def read_icd10_blocks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(ICD10Block).offset(skip).limit(limit).all()


@router.get("/blocks/{id}", response_model=ICD10BlockResponse)
def read_icd10_block(id: str, db: Session = Depends(get_db)):
    db_block = db.query(ICD10Block).filter(ICD10Block.id == id).first()
    if db_block is None:
        raise HTTPException(status_code=404, detail="ICD-10 block not found")
    return db_block


@router.put("/blocks/{id}", response_model=ICD10BlockResponse)
def update_icd10_block(id: str, block: ICD10BlockCreate, db: Session = Depends(get_db)):
    db_block = db.query(ICD10Block).filter(ICD10Block.id == id).first()
    if db_block is None:
        raise HTTPException(status_code=404, detail="ICD-10 block not found")
    for key, value in block.dict().items():
        setattr(db_block, key, value)
    db.commit()
    db.refresh(db_block)
    return db_block


@router.delete("/blocks/{id}", response_model=ICD10BlockResponse)
def delete_icd10_block(id: str, db: Session = Depends(get_db)):
    db_block = db.query(ICD10Block).filter(ICD10Block.id == id).first()
    if db_block is None:
        raise HTTPException(status_code=404, detail="ICD-10 block not found")
    db.delete(db_block)
    db.commit()
    return db_block
