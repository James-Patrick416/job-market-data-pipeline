CREATE TABLE IF NOT EXISTS jobs (
    job_id UUID PRIMARY KEY,

    title VARCHAR(255) NOT NULL,

    company VARCHAR(255),

    location VARCHAR(255),

    job_type VARCHAR(100),

    salary VARCHAR(255),

    description TEXT,

    job_url TEXT UNIQUE NOT NULL,

    scraped_at TIMESTAMP NOT NULL
);