from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import TechCategory, TechProduct

Base.metadata.create_all(bind=engine)
db: Session = SessionLocal()

# Seed categories
categories = ["Laptops", "Smartphones", "Accessories"]
for name in categories:
    if not db.query(TechCategory).filter_by(name=name).first():
        db.add(TechCategory(name=name))
db.commit()

# Seed products
laptop = TechProduct(name="ThinkPad X1", brand="Lenovo", model="X1 Carbon", specs="16GB RAM, 512GB SSD", price=1500.0, stock=10, category_id=1)
smartphone = TechProduct(name="iPhone 15", brand="Apple", model="15 Pro", specs="128GB, A17 Chip", price=1200.0, stock=15, category_id=2)
db.add_all([laptop, smartphone])
db.commit()
db.close()
print("Database seeded.")
