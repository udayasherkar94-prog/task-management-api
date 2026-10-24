import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

# load database settings from the .env file
load_dotenv()

# Read the database configuration

DB_HOST = os.getenv("DB_HOST","localhost")
DB_PORT = os.getenv("DB_PORT","3306")
DB_USER = os.getenv("DB_USER","root")
DB_PASSWORD = os.getenv("DB_PASSWORD","")
DB_NAME = os.getenv("DB_NAME","task_management_db")


# build the Mysql connection URL

DATABASE_URL = ( f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}" f"@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# create databse engine

engine = create_engine(DATABASE_URL,pool_pre_ping=True)

'''What does pool_pre_ping=True do?

Before giving you a connection from the pool, SQLAlchemy sends a tiny test message to the database, basically asking “Are you still there?” (the “ping”).

If the connection answers: it’s used normally.
If it doesn’t answer: SQLAlchemy throws that dead connection away, opens a fresh one, and uses that instead.'''


# Creating sessions
# create a factory for database sessions

SessionLocal = sessionmaker( bind = engine,autoflush=False,autocommit = False)

# Base class for SQLAlchemy models
Base = declarative_base()

# provide a database session to a FastAPI endpoint

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()   
