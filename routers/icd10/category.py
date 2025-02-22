from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import ICD10Category
from schemas.category import ICD10CategoryCreate, ICD10CategoryResponse

router = APIRouter()


@router.post("/categories/", response_model=ICD10CategoryResponse)
def create_icd10_category(category: ICD10CategoryCreate, db: Session = Depends(get_db)):
    db_category = ICD10Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@router.get("/categories/", response_model=List[ICD10CategoryResponse])
def read_icd10_categories(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(ICD10Category).offset(skip).limit(limit).all()


@router.get("/categories/{id}", response_model=ICD10CategoryResponse)
def read_icd10_category(id: str, db: Session = Depends(get_db)):
    db_category = db.query(ICD10Category).filter(ICD10Category.id == id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="ICD-10 category not found")
    return db_category


@router.put("/categories/{id}", response_model=ICD10CategoryResponse)
def update_icd10_category(
    id: str, category: ICD10CategoryCreate, db: Session = Depends(get_db)
):
    db_category = db.query(ICD10Category).filter(ICD10Category.id == id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="ICD-10 category not found")
    for key, value in category.dict().items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category


@router.delete("/categories/{id}", response_model=ICD10CategoryResponse)
def delete_icd10_category(id: str, db: Session = Depends(get_db)):
    db_category = db.query(ICD10Category).filter(ICD10Category.id == id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="ICD-10 category not found")
    db.delete(db_category)
    db.commit()
    return db_category
