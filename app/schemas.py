from typing import Optional

from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None

# what the API sends back to the client. 
# Notice it includes id, which the client doesn't send but Postgres generates.
class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float

    # This tells Pydantic it's okay to read data directly
    #  from a SQLAlchemy object instead of a plain dict.
    #  Without this, returning a database row as a response would crash.
    class Config:
        from_attributes = True