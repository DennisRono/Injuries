from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.icd10 import ICD10Chapter
from schemas.chapter import ICD10ChapterCreate, ICD10ChapterResponse

router = APIRouter()


@router.post("/chapters/", response_model=ICD10ChapterResponse)
def create_icd10_chapter(chapter: ICD10ChapterCreate, db: Session = Depends(get_db)):
    db_chapter = ICD10Chapter(**chapter.dict())
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter


@router.get("/chapters/", response_model=List[ICD10ChapterResponse])
def read_icd10_chapters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    chapters = db.query(ICD10Chapter).offset(skip).limit(limit).all()
    return [
        {
            "id": chapter.id,
            "range_code": chapter.range_code,
            "description": chapter.description,
        }
        for chapter in chapters
    ]


@router.get("/chapters/{id}", response_model=ICD10ChapterResponse)
def read_icd10_chapter(id: str, db: Session = Depends(get_db)):
    db_chapter = db.query(ICD10Chapter).filter(ICD10Chapter.id == id).first()
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="ICD-10 chapter not found")
    return db_chapter


@router.patch("/chapters/{id}", response_model=ICD10ChapterResponse)
def update_icd10_chapter(
    id: str, chapter: ICD10ChapterCreate, db: Session = Depends(get_db)
):
    db_chapter = db.query(ICD10Chapter).filter(ICD10Chapter.id == id).first()
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="ICD-10 chapter not found")
    for key, value in chapter.dict().items():
        setattr(db_chapter, key, value)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter


@router.delete("/chapters/{id}", response_model=ICD10ChapterResponse)
def delete_icd10_chapter(id: str, db: Session = Depends(get_db)):
    db_chapter = db.query(ICD10Chapter).filter(ICD10Chapter.id == id).first()
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="ICD-10 chapter not found")
    db.delete(db_chapter)
    db.commit()
    return db_chapter
