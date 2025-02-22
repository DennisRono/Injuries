from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.claim import Claim
from schemas.claim import ClaimCreate, ClaimResponse

router = APIRouter()


@router.post("/claims/", response_model=ClaimResponse)
def create_claim(claim: ClaimCreate, db: Session = Depends(get_db)):
    db_claim = Claim(**claim.dict())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim


@router.get("/claims/", response_model=List[ClaimResponse])
def read_claims(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Claim).offset(skip).limit(limit).all()


@router.get("/claims/{claim_id}", response_model=ClaimResponse)
def read_claim(claim_id: int, db: Session = Depends(get_db)):
    db_claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if db_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim
