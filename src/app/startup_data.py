from sqlalchemy.orm import Session
from . import models

def initialize_data(db: Session):
    """Create initial categories and products ONLY if database is empty."""

    # Check if categories already exist
    if db.query(models.TechCategory).count() > 0:
        return  # Data already exists

    # --------------------------
    # 1. CREATE CATEGORIES
    # --------------------------
    laptops = models.TechCategory(name="Laptops")
    phones = models.TechCategory(name="Smartphones")
    accessories = models.TechCategory(name="Accessories")

    db.add_all([laptops, phones, accessories])
    db.commit()

    # Refresh to get IDs
    db.refresh(laptops)
    db.refresh(phones)
    db.refresh(accessories)

    # --------------------------
    # 2. CREATE PRODUCTS
    # --------------------------
    sample_products = [
        models.TechProduct(
            name="MacBook Pro 16",
            brand="Apple",
            model="M3 Pro",
            specs="16GB RAM, 1TB SSD, M3 Pro Chip",
            price=3200.00,
            stock=5,
            category_id=laptops.id,
        ),
        models.TechProduct(
            name="Dell XPS 13",
            brand="Dell",
            model="9320",
            specs="16GB RAM, 512GB SSD, Intel i7",
            price=1400.00,
            stock=8,
            category_id=laptops.id,
        ),
        models.TechProduct(
            name="Samsung S24 Ultra",
            brand="Samsung",
            model="SM-S928B",
            specs="12GB RAM, 512GB Storage, 200MP Camera",
            price=1500.00,
            stock=10,
            category_id=phones.id,
        ),
        models.TechProduct(
            name="iPhone 15 Pro",
            brand="Apple",
            model="A17",
            specs="8GB RAM, 256GB Storage, Titanium Frame",
            price=1600.00,
            stock=7,
            category_id=phones.id,
        ),
        models.TechProduct(
            name="Logitech MX Master 3S",
            brand="Logitech",
            model="910-006559",
            specs="Ergonomic mouse, 8 buttons",
            price=120.00,
            stock=20,
            category_id=accessories.id,
        ),
    ]

    db.add_all(sample_products)
    db.commit()

    # Refresh each product so they have ids
    for prod in sample_products:
        db.refresh(prod)

    # --------------------------
    # 3. CREATE EXAMPLE ORDERS
    # --------------------------
    # Use sample_products list (not an undefined 'products' var)
    orders = [
        models.TechOrder(
            quantity=1,
            status="Pending",
            product_id=sample_products[0].id,
            customer_name="John Doe",
            customer_email="john@example.com"
        ),
        models.TechOrder(
            quantity=2,
            status="Shipped",
            product_id=sample_products[2].id,
            customer_name="Alice Smith",
            customer_email="alice@example.com"
        )
    ]

    db.add_all(orders)
    db.commit()
