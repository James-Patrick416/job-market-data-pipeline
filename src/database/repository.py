"""
Repository layer.
"""

from datetime import datetime
from typing import Any

from sqlalchemy.dialects.postgresql import insert

from database.database import SessionLocal
from database.models import Job


class JobRepository:

    def __init__(self):
        self.session = SessionLocal()

    def save_many(
        self,
        jobs: list[dict[str, Any]],
    ) -> int:
        """
        Bulk insert jobs.

        Returns number of inserted rows.
        """

        values = []

        for job in jobs:

            values.append(
                {
                    "title": job["title"],
                    "company": job["company"],
                    "location": job["location"],
                    "job_type": job.get("job_type"),
                    "salary": job.get("salary"),
                    "description": job.get("description"),
                    "job_url": job["job_url"],
                    "scraped_at": datetime.now(),
                }
            )

        statement = (
            insert(Job)
            .values(values)
            .on_conflict_do_nothing(
                index_elements=["job_url"]
            )
        )

        result = self.session.execute(statement)

        self.session.commit()

        return result.rowcount

    def close(self):

        self.session.close()