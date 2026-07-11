"""
Repository layer.

All database interactions are centralized here.

The repository hides SQLAlchemy implementation details from the rest
of the application.
"""

from datetime import datetime
from typing import Any

from sqlalchemy.dialects.postgresql import insert

from database.database import SessionLocal
from database.models import Job


class JobRepository:
    """
    Repository responsible for persisting jobs.
    """

    def __init__(self) -> None:
        self.session = SessionLocal()

    def save(self, job: dict[str, Any]) -> bool:
        """
        Insert a job into PostgreSQL.

        Duplicate job URLs are ignored using PostgreSQL's
        ON CONFLICT DO NOTHING.

        Returns
        -------
        bool
            True if inserted.
            False if skipped.
        """

        statement = (
            insert(Job)
            .values(
                title=job["title"],
                company=job["company"],
                location=job["location"],
                job_type=job.get("job_type"),
                salary=job.get("salary"),
                description=job.get("description"),
                job_url=job["job_url"],
                scraped_at=datetime.now(),
            )
            .on_conflict_do_nothing(
                index_elements=["job_url"]
            )
        )

        result = self.session.execute(statement)
        self.session.commit()

        # PostgreSQL returns one affected row when inserted.
        return result.rowcount == 1

    def close(self) -> None:
        """Close the database session."""
        self.session.close()