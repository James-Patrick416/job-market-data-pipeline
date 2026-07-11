"""
Application specific exceptions.
"""


class PipelineError(Exception):
    """Base exception."""


class ScraperError(PipelineError):
    """Raised when scraping fails."""


class DatabaseError(PipelineError):
    """Raised for database failures."""