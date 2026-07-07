from fastapi import FastAPI
from app.core.config import show_config
from app.database.base import test_database_connection
from app.database.base import create_tables

app = FastAPI(
    title="Rohan AI OS",
    version="0.1.0"
)


@app.on_event("startup")
def startup():
    show_config()
    test_database_connection()
    create_tables()


@app.get("/")
def home():
    return {"message": "Welcome to Rohan AI OS 🚀"}


@app.get("/health")
def health():
    return {"status": "healthy"}