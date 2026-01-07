from fastapi import FastAPI
from .database import engine, Base
from .routers import users


app = FastAPI()

Base.metadata.create_all(bind=engine) # create the sq lite tables automatically on startup

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "User Management System is online"}
