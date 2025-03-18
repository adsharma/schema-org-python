from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.person import Person


class SportsEvent(Event):
    """
    Event type: Sports event.
    """

    homeTeam: Optional[
        Union[Person, List[Person], "SportsTeam", List["SportsTeam"]]
    ] = None
    competitor: Optional[
        Union[Person, List[Person], "SportsTeam", List["SportsTeam"]]
    ] = None
    awayTeam: Optional[
        Union[Person, List[Person], "SportsTeam", List["SportsTeam"]]
    ] = None
    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
