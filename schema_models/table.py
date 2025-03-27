from dataclasses import dataclass

from schema_models.web_page_element import WebPageElement


@dataclass
class Table(WebPageElement):
    """
    A table on a Web page.
    """
