"""
Cleaning layer.
"""

from typing import Any

from cleaning.schemas import JobSchema


def clean_job(job: dict[str, Any]) -> dict[str, Any]:
    """
    Clean and validate one job.
    """

    validated = JobSchema.model_validate(job)

    return validated.model_dump()