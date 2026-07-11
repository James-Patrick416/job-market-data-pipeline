from pprint import pprint

from scraper.client import fetch_page
from scraper.extract import extract_job
from scraper.parser import parse_html

# Website used for learning web scraping.
URL = "https://realpython.github.io/fake-jobs/"

# Download and parse the page.
html = fetch_page(URL)
soup = parse_html(html)

# Find the first job card.
job_card = soup.find("div", class_="card-content")

if job_card is None:
    raise ValueError("No job card found.")

# Extract the job data.
job = extract_job(job_card)

# Pretty-print the dictionary.
pprint(job)