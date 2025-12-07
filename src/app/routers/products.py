from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, crud, deps

router = APIRouter(prefix="/products", tags=["Products"])

# GET products with optional filters
@router.get("/", response_model=List[schemas.TechProduct])
def read_products(
    category_id: Optional[int] = Query(None),
    brand: Optional[str] = Query(None),
    model: Optional[str] = Query(None),
    db: Session = Depends(deps.get_db)
):
    return crud.get_products(db, category_id=category_id, brand=brand, model=model)

# POST new product
@router.post("/", response_model=schemas.TechProduct)
def create_product(product: schemas.TechProduct, db: Session = Depends(deps.get_db)):
    return crud.create_product(db, product)

# PUT update product
@router.put("/{product_id}", response_model=schemas.TechProduct)
def update_product(product_id: int, product: schemas.TechProduct, db: Session = Depends(deps.get_db)):
    try:
        return crud.update_product(db, product_id, product)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# DELETE product
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(deps.get_db)):
    try:
        crud.delete_product(db, product_id)
        return {"message": "Product deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
