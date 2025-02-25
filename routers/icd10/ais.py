from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.ais import AIS
from schemas.ais import AISCreate, AISResponse

router = APIRouter()


@router.post("/ais/", response_model=AISResponse)
def create_ais(ais: AISCreate, db: Session = Depends(get_db)):
    db_ais = AIS(**ais.model_dump())
    db.add(db_ais)
    db.commit()
    db.refresh(db_ais)
    return db_ais


@router.get("/ais/", response_model=List[AISResponse])
def read_ais_codes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(AIS).offset(skip).limit(limit).all()


@router.get("/ais/{code}", response_model=AISResponse)
def read_ais(code: str, db: Session = Depends(get_db)):
    db_ais = db.query(AIS).filter(AIS.code == code).first()
    if db_ais is None:
        raise HTTPException(status_code=404, detail="AIS code not found")
    return db_ais
