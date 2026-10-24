from fastapi import FastAPI

from app.database import Base,engine
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

@app.get("/")
def home():
    return {"message":"Task Management API is running"}

@app.get("/about")
def about():
    return {"Message":"Nothing"}