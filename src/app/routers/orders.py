from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, deps

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", response_model=List[schemas.TechOrder])
def read_orders(db: Session = Depends(deps.get_db)):
    return crud.get_orders(db)

@router.post("/", response_model=schemas.TechOrder)
def create_order(order: schemas.TechOrder, db: Session = Depends(deps.get_db)):
    return crud.create_order(db, order)
