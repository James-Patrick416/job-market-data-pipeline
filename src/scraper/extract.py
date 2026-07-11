from bs4 import Tag


def extract_job(job_card: Tag) -> dict:
    """
    Extract information from a single job card.

    Args:
        job_card: A BeautifulSoup Tag representing one job listing.

    Returns:
        A dictionary containing the job details.
    """

    # Extract the required HTML elements.
    title = job_card.find("h2", class_="title")
    company = job_card.find("h3", class_="company")
    location = job_card.find("p", class_="location")

    # The footer contains the "Apply" link.
    footer = job_card.find("footer")

    # Get the first link inside the footer.
    link = footer.find("a") if footer else None

    return {
        "title": title.get_text(strip=True) if title else None,
        "company": company.get_text(strip=True) if company else None,
        "location": location.get_text(strip=True) if location else None,
        "job_url": link["href"] if link else None,
    }