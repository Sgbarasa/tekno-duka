from pydantic import BaseModel, ConfigDict

# Fix for Python 3.8: use typing.List instead of list[]
from typing import List, Optional

class TechCategory(BaseModel):
    id: Optional[int]
    name: str

    model_config = ConfigDict(from_attributes=True)


class TechProduct(BaseModel):
    id: Optional[int]
    name: str
    price: float
    category_id: int

    brand: Optional[str] = None
    model: Optional[str] = None
    specs: Optional[str] = None
    stock: Optional[int] = 0

    model_config = ConfigDict(from_attributes=True)


class TechOrder(BaseModel):
    id: Optional[int]
    product_id: int
    quantity: int

    # customer and status
    customer_name: Optional[str] = "Guest"
    customer_email: Optional[str] = None
    status: Optional[str] = "Pending"

    model_config = ConfigDict(from_attributes=True)
