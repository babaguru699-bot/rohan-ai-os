from sqlalchemy import text

from app.database.base_class import Base
from app.database.database import engine

# Import all models here
from app.models.user import User


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")


def test_database_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("✅ PostgreSQL Connected Successfully!")
    except Exception as e:
        print(e)