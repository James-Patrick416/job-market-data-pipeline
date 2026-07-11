"""
Repository layer for database operations.

This module is the only part of the application that should communicate
directly with PostgreSQL. It hides SQLAlchemy details from the rest of
the pipeline.
"""

from datetime import datetime
from typing import Any

from sqlalchemy.exc import IntegrityError

from database.database import SessionLocal
from database.models import Job


class JobRepository:
    """
    Repository responsible for CRUD operations on jobs.
    """

    def __init__(self) -> None:
        """
        Create a new database session.
        """
        self.session = SessionLocal()

    def save(self, job: dict[str, Any]) -> bool:
        """
        Save a job to PostgreSQL.

        Args:
            job: Cleaned job dictionary.

        Returns:
            True if inserted successfully.
            False if the job already exists.
        """

        try:
            job_record = Job(
                title=job["title"],
                company=job["company"],
                location=job["location"],
                job_type=job.get("job_type"),
                salary=job.get("salary"),
                description=job.get("description"),
                job_url=job["job_url"],
                scraped_at=datetime.now(),
            )

            self.session.add(job_record)
            self.session.commit()

            return True

        except IntegrityError:
            # Duplicate URL or another constraint violation.
            self.session.rollback()
            return False

    def close(self) -> None:
        """
        Close the current database session.
        """
        self.session.close()