from scraper.client import fetch_page
from scraper.extract import extract_job
from scraper.parser import parse_html


def scrape_jobs(url: str) -> list[dict]:
    """
    Download a page and extract every job listing.

    Args:
        url: The page to scrape.

    Returns:
        A list of job dictionaries.
    """

    # Download the page.
    html = fetch_page(url)

    # Parse the HTML.
    soup = parse_html(html)

    # Find every job card on the page.
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []

    # Extract data from each job card.
    for job_card in job_cards:
        jobs.append(extract_job(job_card))

    return jobs


if __name__ == "__main__":
    URL = "https://realpython.github.io/fake-jobs/"

    jobs = scrape_jobs(URL)

    print(f"Found {len(jobs)} jobs.\n")

    # Display only the first three jobs.
    for job in jobs[:3]:
        print(job)
        print("-" * 60)