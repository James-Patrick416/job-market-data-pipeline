from scraper.client import fetch_page
from scraper.parser import parse_html

# Website used for learning web scraping.
URL = "https://realpython.github.io/fake-jobs/"

# Download the HTML.
html = fetch_page(URL)

# Parse the HTML.
soup = parse_html(html)

# Find the first job card.
job_card = soup.find("div", class_="card-content")

# Ensure a job card was found.
if job_card is None:
    raise ValueError("No job card found on the page.")

# Extract the job title.
title = job_card.find("h2", class_="title")

# Extract the company name.
company = job_card.find("h3", class_="company")

# Extract the location.
location = job_card.find("p", class_="location")

print(f"Title    : {title.get_text(strip=True)}")
print(f"Company  : {company.get_text(strip=True)}")
print(f"Location : {location.get_text(strip=True)}")
