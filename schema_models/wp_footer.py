from dataclasses import dataclass

from schema_models.web_page_element import WebPageElement


@dataclass
class WPFooter(WebPageElement):
    """
    The footer section of the page.
    """
