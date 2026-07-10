from database.database import SessionLocal
from database.models import Job


# Create a database session.
session = SessionLocal()

try:
    # Retrieve all jobs from the database.
    jobs = session.query(Job).all()

    # Print each job in a readable format.
    for job in jobs:
        print("=" * 50)
        print(f"Title      : {job.title}")
        print(f"Company    : {job.company}")
        print(f"Location   : {job.location}")
        print(f"Type       : {job.job_type}")
        print(f"Salary     : {job.salary}")
        print(f"URL        : {job.job_url}")
        print(f"Scraped At : {job.scraped_at}")

finally:
    # Always close the session.
    session.close()