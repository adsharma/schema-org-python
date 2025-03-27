from dataclasses import dataclass

from schema_models.web_page import WebPage


@dataclass
class ProfilePage(WebPage):
    """
    Web page type: Profile page.
    """
