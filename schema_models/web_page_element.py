from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.css_selector_type import CssSelectorType


class WebPageElement(CreativeWork):
    cssSelector: Optional[Union[CssSelectorType, List[CssSelectorType]]] = None
    xpath: Optional[Union[str, List[str]]] = None
