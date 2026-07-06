from app.core.settings import settings


def show_config():
    print("App:", settings.APP_NAME)
    print("Database:", settings.DATABASE_NAME)