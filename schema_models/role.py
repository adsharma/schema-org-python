from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


@dataclass
class Role(Intangible):
    """
    Represents additional information about a relationship or property. For example a Role can be used to say that a 'member' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person's 'actor' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like 'member' or 'actor'.

    See also [blog post](https://blog.schema.org/2014/06/16/introducing-role/).
    """

    endDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    namedPosition: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    roleName: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
