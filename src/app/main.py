from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import categories, products, orders
from .database import engine, SessionLocal
from .models import Base
from .startup_data import initialize_data

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tekno Duka API")

# CORS middleware
origins = [
    "http://localhost:5173",  # Vite dev server
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(orders.router)

# Populate initial data on startup
@app.on_event("startup")
def startup_populate_db():
    db = SessionLocal()
    try:
        initialize_data(db)
    finally:
        db.close()

# Optional debug endpoint
@app.get("/debug")
def debug_db():
    db = SessionLocal()
    try:
        from . import crud
        cats = crud.get_categories(db)
        prods = crud.get_products(db)
        orders_list = crud.get_orders(db)
        return {
            "categories": [c.name for c in cats],
            "products": [p.name for p in prods],
            "orders": [{"product_id": o.product_id, "status": o.status} for o in orders_list],
        }
    finally:
        db.close()
