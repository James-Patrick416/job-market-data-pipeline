import time

import requests

from config.settings import settings
from utils.exceptions import ScraperError
from utils.logger import get_logger

logger = get_logger(__name__)


def fetch_page(url: str) -> str:
    """
    Download a webpage with retries.
    """

    headers = {
        "User-Agent": "JobMarketPipeline/1.0"
    }

    for attempt in range(1, settings.max_retries + 1):

        try:

            logger.info(
                "Fetching %s (attempt %d/%d)",
                url,
                attempt,
                settings.max_retries,
            )

            response = requests.get(
                url,
                headers=headers,
                timeout=settings.request_timeout,
            )

            response.raise_for_status()

            return response.text

        except requests.RequestException as exc:

            logger.warning(
                "Attempt %d failed",
                attempt,
            )

            if attempt == settings.max_retries:
                logger.exception("Unable to fetch page")
                raise ScraperError(
                    f"Could not fetch {url}"
                ) from exc

            # Exponential backoff
            time.sleep(2 ** attempt)

    raise ScraperError("Unexpected failure")