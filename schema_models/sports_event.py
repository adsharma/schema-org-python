from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.event import Event
from schema_models.person import Person
from schema_models.sports_team import SportsTeam
from schema_models.text import Text
from schema_models.url import URL


class SportsEvent(Event):
    homeTeam: Optional[Union[Person, List[Person]]] = None
    homeTeam: Optional[Union[SportsTeam, List[SportsTeam]]] = None
    competitor: Optional[Union[Person, List[Person]]] = None
    competitor: Optional[Union[SportsTeam, List[SportsTeam]]] = None
    awayTeam: Optional[Union[Person, List[Person]]] = None
    awayTeam: Optional[Union[SportsTeam, List[SportsTeam]]] = None
    sport: Optional[Union[Text, List[Text]]] = None
    sport: Optional[Union[URL, List[URL]]] = None
