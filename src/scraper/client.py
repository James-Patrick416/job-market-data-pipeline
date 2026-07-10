import requests


def fetch_page(url: str) -> str:
    """
    Download the HTML content of a web page.

    Args:
        url: The URL of the page to download.

    Returns:
        The HTML content as a string.

    Raises:
        requests.HTTPError: If the request fails.
    """

    # Identify our application to the server.
    headers = {
        "User-Agent": (
            "JobMarketDataPipeline/1.0 "
            "(Educational Project)"
        )
    }

    # Send the HTTP GET request.
    response = requests.get(
        url,
        headers=headers,
        timeout=30,
    )

    # Raise an exception for HTTP errors (404, 500, etc.).
    response.raise_for_status()

    return response.text