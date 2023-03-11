import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.conf.config import settings

load_dotenv()

db_type = os.environ.get('db')
user = os.environ.get('user')
password_db = os.environ.get('password_db')
host = os.environ.get('host')
name_app = os.environ.get('name_app')

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    """
    The get_db function is a context manager that returns the database session.
    It also ensures that the connection to the database is closed after each request.

    :return: A database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
