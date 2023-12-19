from typing import List, Optional

from pydantic import BaseModel


class Variant(BaseModel):
    name: str
    sku: str
    available: bool
    price: float


class Product(BaseModel):
    id: int
    title: str
    variants: Optional[List[Variant]]


item = Product(
    id=123123,
    title="Cool Shirt",
    variants=[
        Variant(
            name="Small",
            sku="ABC123",
            available=True,
            price=24.99
        )
    ]
)

print(item.variants[0].name)