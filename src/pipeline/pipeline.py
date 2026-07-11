"""
Main ETL pipeline.

Pipeline flow

Extract
    ↓
Transform
    ↓
Load
"""

from time import perf_counter

from database.repository import JobRepository
from scraper.scrape_jobs import scrape_jobs
from utils.logger import get_logger

# Create a logger for this module.
logger = get_logger(__name__)


def run_pipeline(url: str) -> None:
    """
    Execute the ETL pipeline.

    Args:
        url: URL to scrape.
    """

    logger.info("Starting ETL pipeline")

    start_time = perf_counter()

    repository = JobRepository()

    inserted = 0
    skipped = 0

    try:
        # Extract and clean jobs.
        jobs = scrape_jobs(url)

        logger.info("Extracted %d jobs", len(jobs))

        # Load jobs into PostgreSQL.
        for job in jobs:

            if repository.save(job):
                inserted += 1
            else:
                skipped += 1

        duration = perf_counter() - start_time

        logger.info("Inserted %d jobs", inserted)
        logger.info("Skipped %d duplicate jobs", skipped)
        logger.info("Pipeline finished in %.2f seconds", duration)

    except Exception:
        # Logs the exception together with the full traceback.
        logger.exception("Pipeline execution failed")
        raise

    finally:
        repository.close()


def main() -> None:
    """
    Development entry point.
    """

    url = "https://realpython.github.io/fake-jobs/"

    run_pipeline(url)


if __name__ == "__main__":
    main()