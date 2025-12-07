from src.app.database import SessionLocal
from src.app.models import TechCategory, TechProduct, TechOrder
from src.app.startup_data import initialize_data

def main():
    db = SessionLocal()
    
    # Populate initial data (only if empty)
    initialize_data(db)

    # Fetch and print all data
    categories = db.query(TechCategory).all()
    products = db.query(TechProduct).all()
    orders = db.query(TechOrder).all()

    print("=== Categories ===")
    for c in categories:
        print(f"{c.id}: {c.name}")

    print("\n=== Products ===")
    for p in products:
        print(f"{p.id}: {p.name} ({p.brand} {p.model}) - Category ID: {p.category_id} - Stock: {p.stock}")

    print("\n=== Orders ===")
    for o in orders:
        print(f"{o.id}: Product ID {o.product_id}, Qty {o.quantity}, Customer {o.customer_name}, Status {o.status}")

    db.close()

if __name__ == "__main__":
    main()
