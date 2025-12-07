from fastapi import FastAPI
from .routers import categories, products, orders
from .database import engine
from .models import Base
from .database import SessionLocal
from .startup_data import initialize_data

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tekno Duka API")

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
