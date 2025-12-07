from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, deps

router = APIRouter(prefix="/categories", tags=["Categories"])

# GET all categories
@router.get("/", response_model=List[schemas.TechCategory])
def read_categories(db: Session = Depends(deps.get_db)):
    return crud.get_categories(db)

# POST new category
@router.post("/", response_model=schemas.TechCategory)
def create_category(category: schemas.TechCategory, db: Session = Depends(deps.get_db)):
    return crud.create_category(db, category)

# PUT update category
@router.put("/{category_id}", response_model=schemas.TechCategory)
def update_category(category_id: int, category: schemas.TechCategory, db: Session = Depends(deps.get_db)):
    try:
        return crud.update_category(db, category_id, category)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# DELETE category
@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(deps.get_db)):
    try:
        crud.delete_category(db, category_id)
        return {"message": "Category deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
