from typing import Any


def clean_job(job: dict[str, Any]) -> dict[str, Any]:
    """
    Clean a single scraped job.

    Args:
        job: Raw job data extracted from the website.

    Returns:
        A cleaned job dictionary.
    """

    # Make a copy so we don't modify the original data.
    cleaned = job.copy()

    # Clean string fields.
    for field in ["title", "company", "location", "job_url"]:
        value = cleaned.get(field)

        if isinstance(value, str):
            # Remove leading/trailing whitespace.
            value = value.strip()

            # Replace multiple spaces with a single space.
            value = " ".join(value.split())

            cleaned[field] = value

    return cleaned