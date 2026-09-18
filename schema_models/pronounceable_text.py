from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.text import Text


@dataclass
class PronounceableText(Text):
    """
    Data type: PronounceableText.
    """

    inLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = None
    phoneticText: Optional[Union[str, List[str]]] = None
    speechToTextMarkup: Optional[Union[str, List[str]]] = None
    textValue: Optional[Union[str, List[str]]] = None
