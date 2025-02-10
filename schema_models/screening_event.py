from typing import List, Optional, Union

from schema_models.event import Event


class ScreeningEvent(Event):
    """
    A screening of a movie or other video.
    """

    videoFormat: Optional[Union[str, List[str]]] = None
    subtitleLanguage: Optional[Union[str, List[str]]] = None
    subtitleLanguage: Optional[Union["Language", List["Language"]]] = None
    workPresented: Optional[Union["Movie", List["Movie"]]] = None
