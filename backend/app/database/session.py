"""Session helpers for database access."""

from app.database.database import SessionLocal


def get_session():
    """Yield a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
