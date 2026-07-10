import uuid

from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase


# Base class that all database models will inherit from.
# SQLAlchemy uses this to keep track of all tables.
class Base(DeclarativeBase):
    pass


# Represents the "jobs" table in PostgreSQL.
class Job(Base):
    # Name of the table in the database.
    __tablename__ = "jobs"

    # Primary key generated automatically using UUID.
    job_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Job title (required).
    title = Column(String(255), nullable=False)

    # Company offering the job.
    company = Column(String(255))

    # Job location.
    location = Column(String(255))

    # Employment type (Full-time, Contract, etc.).
    job_type = Column(String(100))

    # Salary as advertised.
    salary = Column(String(255))

    # Complete job description.
    description = Column(Text)

    # Original URL of the job posting.
    # Must be unique to prevent duplicate records.
    job_url = Column(Text, unique=True, nullable=False)

    # Timestamp indicating when the job was scraped.
    scraped_at = Column(DateTime, nullable=False)