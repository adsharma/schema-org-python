from typing import List, Optional, Union

from schema_models.css_selector_type import CssSelectorType
from schema_models.intangible import Intangible


class SpeakableSpecification(Intangible):
    """
    A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property.
    """

    cssSelector: Optional[Union[CssSelectorType, List[CssSelectorType]]] = None
    xpath: Optional[Union[str, List[str]]] = None
