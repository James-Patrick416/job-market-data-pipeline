from bs4 import BeautifulSoup


def parse_html(html: str) -> BeautifulSoup:
    """
    Convert raw HTML into a BeautifulSoup object.

    Args:
        html: The HTML content of a web page.

    Returns:
        A BeautifulSoup object that can be searched.
    """

    # Use lxml because it is fast and robust.
    soup = BeautifulSoup(html, "lxml")

    return soup