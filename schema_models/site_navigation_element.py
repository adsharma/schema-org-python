from dataclasses import dataclass

from schema_models.web_page_element import WebPageElement


@dataclass
class SiteNavigationElement(WebPageElement):
    """
    A navigation element of the page.
    """
