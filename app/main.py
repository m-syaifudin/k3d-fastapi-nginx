from fastapi import FastAPI

from app.database import Base, engine
from app.routers import items

# SQLAlchemy needs to know about your models before it can create the tables
# this write after create database and models files.
Base.metadata.create_all(bind=engine)

# create your app instance. 
# title and version show up in the auto-generated docs at /docs.
app = FastAPI(title="FastAPI CRUD", version="1.0.0")

app.include_router(items.router)

# register a route. 
# When someone sends a GET request to /health, run the function below it.
@app.get("/health")

# just a normal Python function. 
# FastAPI calls it automatically when the route is hit.
def health():
    return {"status": "ok"}
