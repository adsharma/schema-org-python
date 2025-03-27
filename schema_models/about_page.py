from dataclasses import dataclass

from schema_models.web_page import WebPage


@dataclass
class AboutPage(WebPage):
    """
    Web page type: About page.
    """
