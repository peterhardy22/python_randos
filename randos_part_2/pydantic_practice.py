import json
from typing import List, Optional

from pydantic import BaseModel, field_validator


class Variant(BaseModel):
    name: str
    sku: str
    available: bool
    price: float

    @field_validator("sku")
    def sku_length(cls, value) -> str:
        if len(value) != 7:
            raise ValueError("SKU must be 7 characters long.")
        return value


class Product(BaseModel):
    id: int
    title: str
    variants: Optional[List[Variant]]


if __name__ == "__main__":

    with open("randos_part_2/data.json") as f:
        data = json.load(f)
        items = [Product(**item) for item in data ["results"]]

    print(items)