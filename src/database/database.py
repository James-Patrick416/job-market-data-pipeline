import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables from the .env file
load_dotenv()

# Build the PostgreSQL connection URL using environment variables
DATABASE_URL = (
    f"postgresql+psycopg://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@localhost:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Create a SQLAlchemy Engine.
# The engine manages the connection pool and communicates with PostgreSQL.
engine = create_engine(
    DATABASE_URL,
    echo=True,      # Log all SQL statements (useful while learning)
    future=True     # Enable SQLAlchemy 2.0 style behavior
)

# Create a Session factory.
# Calling SessionLocal() gives us a new database session.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)