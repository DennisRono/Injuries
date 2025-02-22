from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import ICD10Subcategory
from schemas.sub_category import ICD10SubcategoryCreate, ICD10SubcategoryResponse

router = APIRouter()


@router.post("/subcategories/", response_model=ICD10SubcategoryResponse)
def create_icd10_subcategory(
    subcategory: ICD10SubcategoryCreate, db: Session = Depends(get_db)
):
    db_subcategory = ICD10Subcategory(**subcategory.dict())
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory


@router.get("/subcategories/", response_model=List[ICD10SubcategoryResponse])
def read_icd10_subcategories(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(ICD10Subcategory).offset(skip).limit(limit).all()


@router.get("/subcategories/{id}", response_model=ICD10SubcategoryResponse)
def read_icd10_subcategory(id: str, db: Session = Depends(get_db)):
    db_subcategory = (
        db.query(ICD10Subcategory).filter(ICD10Subcategory.id == id).first()
    )
    if db_subcategory is None:
        raise HTTPException(status_code=404, detail="ICD-10 subcategory not found")
    return db_subcategory


@router.put("/subcategories/{id}", response_model=ICD10SubcategoryResponse)
def update_icd10_subcategory(
    id: str, subcategory: ICD10SubcategoryCreate, db: Session = Depends(get_db)
):
    db_subcategory = (
        db.query(ICD10Subcategory).filter(ICD10Subcategory.id == id).first()
    )
    if db_subcategory is None:
        raise HTTPException(status_code=404, detail="ICD-10 subcategory not found")
    for key, value in subcategory.dict().items():
        setattr(db_subcategory, key, value)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory


@router.delete("/subcategories/{id}", response_model=ICD10SubcategoryResponse)
def delete_icd10_subcategory(id: str, db: Session = Depends(get_db)):
    db_subcategory = (
        db.query(ICD10Subcategory).filter(ICD10Subcategory.id == id).first()
    )
    if db_subcategory is None:
        raise HTTPException(status_code=404, detail="ICD-10 subcategory not found")
    db.delete(db_subcategory)
    db.commit()
    return db_subcategory
