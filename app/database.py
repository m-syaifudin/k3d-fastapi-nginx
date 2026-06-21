import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# reads the connection string from an environment variable. 
# If not set, falls back to the default. 
# This is important later when running in Kubernetes,
# you just change the env var, not the code.
DATABASE_URL = os.getenv("DATABASE_URL",
                          "postgresql://postgres:password@localhost:5432/cruddb")

# creates the actual connection to Postgres.
engine = create_engine(DATABASE_URL)

# a factory that creates database sessions. Each request gets its own session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# the base class your models will inherit from. 
# This is how SQLAlchemy knows what tables to create.
Base = declarative_base()

#  a dependency function. 
#  FastAPI calls this automatically on each request, gives you a db session, 
# and closes it cleanly when the request is done. The yield is what makes that work.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
