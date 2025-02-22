from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import ICD10MiniCategory
from schemas.mini_category import ICD10MiniCategoryCreate, ICD10MiniCategoryResponse

router = APIRouter()


@router.post("/mini-categories/", response_model=ICD10MiniCategoryResponse)
def create_icd10_mini_category(
    mini_category: ICD10MiniCategoryCreate, db: Session = Depends(get_db)
):
    db_mini_category = ICD10MiniCategory(**mini_category.dict())
    db.add(db_mini_category)
    db.commit()
    db.refresh(db_mini_category)
    return db_mini_category


@router.get("/mini-categories/", response_model=List[ICD10MiniCategoryResponse])
def read_icd10_mini_categories(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return db.query(ICD10MiniCategory).offset(skip).limit(limit).all()


@router.get("/mini-categories/{id}", response_model=ICD10MiniCategoryResponse)
def read_icd10_mini_category(id: str, db: Session = Depends(get_db)):
    db_mini_category = (
        db.query(ICD10MiniCategory).filter(ICD10MiniCategory.id == id).first()
    )
    if db_mini_category is None:
        raise HTTPException(status_code=404, detail="ICD-10 mini category not found")
    return db_mini_category


@router.put("/mini-categories/{id}", response_model=ICD10MiniCategoryResponse)
def update_icd10_mini_category(
    id: str, mini_category: ICD10MiniCategoryCreate, db: Session = Depends(get_db)
):
    db_mini_category = (
        db.query(ICD10MiniCategory).filter(ICD10MiniCategory.id == id).first()
    )
    if db_mini_category is None:
        raise HTTPException(status_code=404, detail="ICD-10 mini category not found")
    for key, value in mini_category.dict().items():
        setattr(db_mini_category, key, value)
    db.commit()
    db.refresh(db_mini_category)
    return db_mini_category


@router.delete("/mini-categories/{id}", response_model=ICD10MiniCategoryResponse)
def delete_icd10_mini_category(id: str, db: Session = Depends(get_db)):
    db_mini_category = (
        db.query(ICD10MiniCategory).filter(ICD10MiniCategory.id == id).first()
    )
    if db_mini_category is None:
        raise HTTPException(status_code=404, detail="ICD-10 mini category not found")
    db.delete(db_mini_category)
    db.commit()
    return db_mini_category
