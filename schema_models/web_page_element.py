from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.css_selector_type import CssSelectorType


class WebPageElement(CreativeWork):
    """
    A web page element, like a table or an image.
    """

    cssSelector: Optional[Union[CssSelectorType, List[CssSelectorType]]] = None
    xpath: Optional[Union[str, List[str]]] = None
