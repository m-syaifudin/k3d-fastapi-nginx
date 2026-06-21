from sqlalchemy import Column, Float, Integer, String

from app.database import Base

# inherit from the Base we created in database.py. 
# This is how SQLAlchemy knows this class represents a database table.
class Item(Base):
    # the actual table name in Postgres. 
    # What you put here is what you'll see in the database.
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

