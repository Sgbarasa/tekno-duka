from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

# --------------------------
# Categories
# --------------------------
def get_categories(db: Session) -> List[models.TechCategory]:
    return db.query(models.TechCategory).all()

def create_category(db: Session, category: schemas.TechCategory) -> models.TechCategory:
    db_category = models.TechCategory(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category: schemas.TechCategory) -> models.TechCategory:
    db_category = db.query(models.TechCategory).get(category_id)
    if not db_category:
        raise ValueError("Category not found")
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(models.TechCategory).get(category_id)
    if not db_category:
        raise ValueError("Category not found")
    db.delete(db_category)
    db.commit()

# --------------------------
# Products
# --------------------------
def get_products(
    db: Session,
    category_id: Optional[int] = None,
    brand: Optional[str] = None,
    model: Optional[str] = None
) -> List[models.TechProduct]:
    q = db.query(models.TechProduct)
    if category_id:
        q = q.filter(models.TechProduct.category_id == category_id)
    if brand:
        q = q.filter(models.TechProduct.brand.ilike(f"%{brand}%"))
    if model:
        q = q.filter(models.TechProduct.model.ilike(f"%{model}%"))
    return q.all()

def create_product(db: Session, product: schemas.TechProduct) -> models.TechProduct:
    db_product = models.TechProduct(
        name=product.name,
        price=product.price,
        category_id=product.category_id,
        brand=product.brand,
        model=product.model,
        specs=product.specs,
        stock=product.stock or 0
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: schemas.TechProduct) -> models.TechProduct:
    db_product = db.query(models.TechProduct).get(product_id)
    if not db_product:
        raise ValueError("Product not found")
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.TechProduct).get(product_id)
    if not db_product:
        raise ValueError("Product not found")
    db.delete(db_product)
    db.commit()

# --------------------------
# Orders
# --------------------------
def get_orders(db: Session) -> List[models.TechOrder]:
    return db.query(models.TechOrder).all()

def create_order(db: Session, order: schemas.TechOrder) -> models.TechOrder:
    db_order = models.TechOrder(
        product_id=order.product_id,
        quantity=order.quantity,
        customer_name=order.customer_name,
        customer_email=order.customer_email,
        status=order.status or "Pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
