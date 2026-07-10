from datetime import datetime

from database.database import SessionLocal
from database.models import Job


# Create a new database session.
session = SessionLocal()

try:
    # Create a sample job object.
    sample_job = Job(
        title="Junior Data Engineer",
        company="Acme Technologies",
        location="Nairobi, Kenya",
        job_type="Full-time",
        salary="KES 120,000",
        description="Build and maintain ETL pipelines.",
        job_url="https://example.com/jobs/1",
        scraped_at=datetime.now(),
    )

    # Stage the object for insertion.
    session.add(sample_job)

    # Save the changes to PostgreSQL.
    session.commit()

    print("✅ Sample job inserted successfully.")

except Exception as error:
    # Undo the transaction if something goes wrong.
    session.rollback()
    print(f"❌ Error: {error}")

finally:
    # Always close the session to release the connection.
    session.close()