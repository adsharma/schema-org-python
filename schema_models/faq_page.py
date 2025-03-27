from dataclasses import dataclass

from schema_models.web_page import WebPage


@dataclass
class FAQPage(WebPage):
    """
    A [[FAQPage]] is a [[WebPage]] presenting one or more "[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)" (see also [[QAPage]]).
    """
