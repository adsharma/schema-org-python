from dataclasses import dataclass

from schema_models.web_page import WebPage


@dataclass
class ItemPage(WebPage):
    """
    A page devoted to a single item, such as a particular product or hotel.
    """
