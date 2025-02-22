from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.injury import Injury
from schemas.injury import InjuryCreate, InjuryResponse
from services.injury_severity import calculate_iss

router = APIRouter()


@router.post("/injuries/", response_model=InjuryResponse)
def create_injury(injury: InjuryCreate, db: Session = Depends(get_db)):
    db_injury = Injury(**injury.dict())
    db.add(db_injury)
    db.commit()
    db.refresh(db_injury)
    return db_injury


@router.get("/injuries/", response_model=List[InjuryResponse])
def read_injuries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return [injury for injury in db.query(Injury).offset(skip).limit(limit).all()]


@router.get("/injuries/{injury_id}", response_model=InjuryResponse)
def read_injury(injury_id: int, db: Session = Depends(get_db)):
    db_injury = db.query(Injury).filter(Injury.id == injury_id).first()
    if db_injury is None:
        raise HTTPException(status_code=404, detail="Injury not found")
    return db_injury


@router.get("/injuries/{injury_id}/iss")
def get_injury_severity_score(injury_id: int, db: Session = Depends(get_db)):
    db_injury = db.query(Injury).filter(Injury.id == injury_id).first()
    if db_injury is None:
        raise HTTPException(status_code=404, detail="Injury not found")
    iss = calculate_iss(db_injury.ais.severity)
    return {"injury_id": injury_id, "iss": iss}
