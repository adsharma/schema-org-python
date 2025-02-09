from typing import List, Optional, Union

from schema_models.text import Text


class PronounceableText(Text):
    textValue: Optional[Union[str, List[str]]] = None
    inLanguage: Optional[Union["Language", List["Language"]]] = None
    inLanguage: Optional[Union[str, List[str]]] = None
    speechToTextMarkup: Optional[Union[str, List[str]]] = None
    phoneticText: Optional[Union[str, List[str]]] = None
