from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.movie import Movie


@dataclass
class ScreeningEvent(Event):
    """
    A screening of a movie or other video.
    """

    subtitleLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = (
        None
    )
    videoFormat: Optional[Union[str, List[str]]] = None
    workPresented: Optional[Union[Movie, List[Movie]]] = None
