"""
Validation schemas.

All scraped data must pass validation before entering the database.
"""

from pydantic import BaseModel, HttpUrl, field_validator


class JobSchema(BaseModel):
    """
    Validated job record.
    """

    title: str
    company: str | None = None
    location: str | None = None
    job_type: str | None = None
    salary: str | None = None
    description: str | None = None
    job_url: HttpUrl

    @field_validator(
        "title",
        "company",
        "location",
        "job_type",
        "salary",
        mode="before",
    )
    @classmethod
    def clean_strings(cls, value):

        if value is None:
            return None

        return " ".join(str(value).split())