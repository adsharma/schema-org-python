from dataclasses import dataclass

from schema_models.web_page import WebPage


@dataclass
class SearchResultsPage(WebPage):
    """
    Web page type: Search results page.
    """
