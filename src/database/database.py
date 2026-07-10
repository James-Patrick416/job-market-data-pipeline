from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@localhost:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL, echo=True)