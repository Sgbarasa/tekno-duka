from sqlalchemy.orm import Session
from . import models, schemas

# Categories
def get_categories(db: Session):
    return db.query(models.TechCategory).all()

def create_category(db: Session, category: schemas.TechCategory):
    db_category = models.TechCategory(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Products
def get_products(db: Session):
    return db.query(models.TechProduct).all()

def create_product(db: Session, product: schemas.TechProduct):
    db_product = models.TechProduct(
        name=product.name,
        price=product.price,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Orders
def get_orders(db: Session):
    return db.query(models.TechOrder).all()

def create_order(db: Session, order: schemas.TechOrder):
    db_order = models.TechOrder(
        product_id=order.product_id,
        quantity=order.quantity
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
