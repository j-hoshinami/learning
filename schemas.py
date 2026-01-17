from typing import Optional

from pydantic import BaseModel


class Animal(BaseModel):
    name: str
    race: str
    age: int
    is_alive: Optional[bool]
    weight: float
