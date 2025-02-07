from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.text import Text


class ScreeningEvent(Event):
    videoFormat: Optional[Union[Text, List[Text]]] = None
    subtitleLanguage: Optional[Union[Text, List[Text]]] = None
    subtitleLanguage: Optional[Union["Language", List["Language"]]] = None
    workPresented: Optional[Union["Movie", List["Movie"]]] = None
