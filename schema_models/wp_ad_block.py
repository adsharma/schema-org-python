from dataclasses import dataclass

from schema_models.web_page_element import WebPageElement


@dataclass
class WPAdBlock(WebPageElement):
    """
    An advertising section of the page.
    """
