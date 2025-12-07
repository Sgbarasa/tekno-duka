from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, crud, deps

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[schemas.TechProduct])
def read_products(
    category_id: Optional[int] = Query(None),
    db: Session = Depends(deps.get_db)
):
    return crud.get_products(db, category_id=category_id)

@router.post("/", response_model=schemas.TechProduct)
def create_product(product: schemas.TechProduct, db: Session = Depends(deps.get_db)):
    return crud.create_product(db, product)
