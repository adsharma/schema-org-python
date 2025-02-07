from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.event import Event
from schema_models.language import Language
from schema_models.movie import Movie
from schema_models.text import Text


class ScreeningEvent(Event):
    videoFormat: Optional[Union[Text, List[Text]]] = None
    subtitleLanguage: Optional[Union[Text, List[Text]]] = None
    subtitleLanguage: Optional[Union[Language, List[Language]]] = None
    workPresented: Optional[Union[Movie, List[Movie]]] = None
