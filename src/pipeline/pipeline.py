"""
Main ETL pipeline.

Pipeline flow:

1. Extract job listings from a website.
2. Clean the extracted data.
3. Load the cleaned data into PostgreSQL.
4. Print a pipeline summary.

This module coordinates the entire application.
"""

from scraper.scrape_jobs import scrape_jobs
from database.repository import JobRepository


def run_pipeline(url: str) -> None:
    """
    Execute the complete ETL pipeline.

    Args:
        url: URL of the page to scrape.
    """

    repository = JobRepository()

    inserted = 0
    skipped = 0

    try:
        # Extract and clean all jobs.
        jobs = scrape_jobs(url)

        # Load each job into PostgreSQL.
        for job in jobs:
            success = repository.save(job)

            if success:
                inserted += 1
            else:
                skipped += 1

        # Print pipeline summary.
        print("\nPipeline completed successfully.")
        print("-" * 40)
        print(f"Jobs scraped : {len(jobs)}")
        print(f"Inserted     : {inserted}")
        print(f"Skipped      : {skipped}")

    finally:
        # Always release the database connection.
        repository.close()


def main() -> None:
    """
    Development entry point.
    """

    url = "https://realpython.github.io/fake-jobs/"

    run_pipeline(url)


if __name__ == "__main__":
    main()