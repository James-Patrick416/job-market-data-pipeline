"""
Scraping orchestration.

This module coordinates the extraction phase of the ETL pipeline by:

1. Downloading the HTML page.
2. Parsing the HTML.
3. Extracting every job listing.
4. Cleaning the extracted data.

The result is a list of clean Python dictionaries ready for loading into
the database.
"""

from typing import Any

from cleaning.clean_jobs import clean_job
from scraper.client import fetch_page
from scraper.extract import extract_job
from scraper.parser import parse_html


def scrape_jobs(url: str) -> list[dict[str, Any]]:
    """
    Scrape all jobs from a single page.

    Args:
        url: URL of the page to scrape.

    Returns:
        A list of cleaned job dictionaries.
    """

    # Download the webpage.
    html = fetch_page(url)

    # Parse the HTML into a BeautifulSoup object.
    soup = parse_html(html)

    # Locate every job card.
    job_cards = soup.find_all("div", class_="card-content")

    jobs: list[dict[str, Any]] = []

    # Extract and clean each job.
    for job_card in job_cards:
        raw_job = extract_job(job_card)
        cleaned_job = clean_job(raw_job)
        jobs.append(cleaned_job)

    return jobs


def main() -> None:
    """
    Entry point used during development.

    Scrapes one page and prints a small preview.
    """

    url = "https://realpython.github.io/fake-jobs/"

    jobs = scrape_jobs(url)

    print(f"\nSuccessfully scraped {len(jobs)} jobs.\n")

    # Display the first three jobs.
    for index, job in enumerate(jobs[:3], start=1):
        print(f"Job {index}")
        print("-" * 50)

        for key, value in job.items():
            print(f"{key:<10}: {value}")

        print()


if __name__ == "__main__":
    main()