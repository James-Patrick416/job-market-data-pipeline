"""
ETL Pipeline
"""

from time import perf_counter

from config.settings import settings
from database.repository import JobRepository
from scraper.scrape_jobs import scrape_jobs
from utils.logger import get_logger

logger = get_logger(__name__)


def run_pipeline():

    logger.info("Pipeline started")

    start = perf_counter()

    repository = JobRepository()

    try:

        jobs = scrape_jobs(settings.base_url)

        inserted = repository.save_many(jobs)

        skipped = len(jobs) - inserted

        logger.info("Scraped : %d", len(jobs))
        logger.info("Inserted: %d", inserted)
        logger.info("Skipped : %d", skipped)
        logger.info(
            "Finished in %.2f seconds",
            perf_counter() - start,
        )

    finally:
        repository.close()


if __name__ == "__main__":
    run_pipeline()