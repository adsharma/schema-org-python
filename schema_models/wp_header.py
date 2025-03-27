from dataclasses import dataclass

from schema_models.web_page_element import WebPageElement


@dataclass
class WPHeader(WebPageElement):
    """
    The header section of the page.
    """
