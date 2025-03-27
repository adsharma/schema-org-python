from dataclasses import dataclass

from schema_models.web_page import WebPage


@dataclass
class CheckoutPage(WebPage):
    """
    Web page type: Checkout page.
    """
