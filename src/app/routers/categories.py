from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, deps

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[schemas.TechCategory])
def read_categories(db: Session = Depends(deps.get_db)):
    return crud.get_categories(db)

@router.post("/", response_model=schemas.TechCategory)
def create_category(category: schemas.TechCategory, db: Session = Depends(deps.get_db)):
    return crud.create_category(db, category)
