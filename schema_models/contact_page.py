from dataclasses import dataclass

from schema_models.web_page import WebPage


@dataclass
class ContactPage(WebPage):
    """
    Web page type: Contact page.
    """
