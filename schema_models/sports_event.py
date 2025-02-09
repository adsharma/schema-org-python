from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.person import Person


class SportsEvent(Event):
    homeTeam: Optional[Union[Person, List[Person]]] = None
    homeTeam: Optional[Union["SportsTeam", List["SportsTeam"]]] = None
    competitor: Optional[Union[Person, List[Person]]] = None
    competitor: Optional[Union["SportsTeam", List["SportsTeam"]]] = None
    awayTeam: Optional[Union[Person, List[Person]]] = None
    awayTeam: Optional[Union["SportsTeam", List["SportsTeam"]]] = None
    sport: Optional[Union[str, List[str]]] = None
    sport: Optional[Union[HttpUrl, List[HttpUrl]]] = None
