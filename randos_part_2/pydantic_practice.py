from typing import List, Optional

from pydantic import BaseModel, field_validator


class Variant(BaseModel):
    name: str
    sku: str
    available: bool
    price: float

    @field_validator("sku")
    def sku_length(cls, value):
        if len(value) != 7:
            raise ValueError("SKU must be 7 characters long.")


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
            sku="ABC1234",
            available=True,
            price=24.99
        ),
        Variant(
            name="Medium",
            sku="ABC1235",
            available="False",
            price=25
        )
    ]
)

print(item)