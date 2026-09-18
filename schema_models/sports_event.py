from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.person import Person


@dataclass
class SportsEvent(Event):
    """
    A sub property of location. The sports event where this action occurred.
    """

    awayTeam: Optional[
        Union[Person, List[Person], "SportsTeam", List["SportsTeam"]]
    ] = None
    competitor: Optional[
        Union[Person, List[Person], "SportsTeam", List["SportsTeam"]]
    ] = None
    homeTeam: Optional[
        Union[Person, List[Person], "SportsTeam", List["SportsTeam"]]
    ] = None
    referee: Optional[Union[Person, List[Person]]] = None
    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
