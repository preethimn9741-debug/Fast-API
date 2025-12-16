from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

def _init_(self, id: int, name: str, description: str, quantity: int, price: str):
    self.id = id
    self.name = name
    self.description = description
    self.price = price
    self.quantity = quantity
