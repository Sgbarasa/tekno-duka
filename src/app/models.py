from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class TechCategory(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    products = relationship("TechProduct", back_populates="category")


class TechProduct(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    stock = Column(Integer)
    # Make sure these exist if you want to use them:
    brand = Column(String)       # <--- must match what you pass in startup_data
    model = Column(String)
    specs = Column(String)
    category = relationship("TechCategory", back_populates="products")
    orders = relationship("TechOrder", back_populates="product")


class TechOrder(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)

    # customer info + order status
    customer_name = Column(String, nullable=True)
    customer_email = Column(String, nullable=True)
    status = Column(String, default="Pending")

    product = relationship("TechProduct", back_populates="orders") 