from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import ClassificationGroup
from schemas.classification_group import (
    ClassificationGroupCreate,
    ClassificationGroupResponse,
)

router = APIRouter()


@router.post("/classification-groups/", response_model=ClassificationGroupResponse)
def create_icd10_classification_group(
    group: ClassificationGroupCreate, db: Session = Depends(get_db)
):
    db_classification_group = ClassificationGroup(**group.model_dump())
    db.add(db_classification_group)
    db.commit()
    db.refresh(db_classification_group)
    return db_classification_group


@router.get("/classification-group/", response_model=List[ClassificationGroupResponse])
def read_icd10_classification_groups(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    classification_groups = (
        db.query(ClassificationGroup).offset(skip).limit(limit).all()
    )
    return [classification_group for classification_group in classification_groups]


@router.get("/classification-group/{id}", response_model=ClassificationGroupResponse)
def read_icd10_classification_group(code_range: str, db: Session = Depends(get_db)):
    db_classification_group = (
        db.query(ClassificationGroup)
        .filter(ClassificationGroup.range_code == code_range)
        .first()
    )
    if db_classification_group is None:
        raise HTTPException(
            status_code=404, detail="ICD-10 classification_group not found"
        )
    return db_classification_group


@router.patch(
    "/classification-group/{range_code}", response_model=ClassificationGroupResponse
)
def update_icd10_classification_group(
    range_code: str,
    classification_group: ClassificationGroupCreate,
    db: Session = Depends(get_db),
):
    db_classification_group = (
        db.query(ClassificationGroup)
        .filter(ClassificationGroup.range_code == range_code)
        .first()
    )
    if db_classification_group is None:
        raise HTTPException(
            status_code=404, detail="ICD-10 Classification Group not found"
        )
    for key, value in classification_group.dict().items():
        setattr(db_classification_group, key, value)
    db.commit()
    db.refresh(db_classification_group)
    return db_classification_group


@router.delete("/classification-group/{id}", response_model=ClassificationGroupResponse)
def delete_icd10_classification_group(range_code: str, db: Session = Depends(get_db)):
    db_classification_group = (
        db.query(ClassificationGroup)
        .filter(ClassificationGroup.range_code == range_code)
        .first()
    )
    if db_classification_group is None:
        raise HTTPException(
            status_code=404, detail="ICD-10 classification_group not found"
        )
    db.delete(db_classification_group)
    db.commit()
    return db_classification_group
