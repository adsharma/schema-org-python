from dataclasses import dataclass

from schema_models.web_page_element import WebPageElement


@dataclass
class WPSideBar(WebPageElement):
    """
    A sidebar section of the page.
    """
