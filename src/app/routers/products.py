from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, deps

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[schemas.TechProduct])
def read_products(db: Session = Depends(deps.get_db)):
    return crud.get_products(db)

@router.post("/", response_model=schemas.TechProduct)
def create_product(product: schemas.TechProduct, db: Session = Depends(deps.get_db)):
    return crud.create_product(db, product)
