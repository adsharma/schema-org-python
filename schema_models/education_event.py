from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.text import Text
from schema_models.url import URL


class EducationEvent(Event):
    teaches: Optional[Union[Text, List[Text]]] = None
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    assesses: Optional[Union[Text, List[Text]]] = None
    educationalLevel: Optional[Union[Text, List[Text]]] = None
    educationalLevel: Optional[Union[URL, List[URL]]] = None
    educationalLevel: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
