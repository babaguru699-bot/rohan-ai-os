from app.database.database import engine


def test_database_connection():
    try:
        with engine.connect() as connection:
            print("✅ PostgreSQL Connected Successfully!")
    except Exception as e:
        print("❌ Database Connection Failed")
        print(e)