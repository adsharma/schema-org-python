from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class CreativeWorkSeason(CreativeWork):
    """
    A media season, e.g. TV, radio, video game etc.
    """

    actor: Optional[
        Union["PerformingGroup", List["PerformingGroup"], Person, List[Person]]
    ] = None
    director: Optional[Union[Person, List[Person]]] = None
    endDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    episode: Optional[Union["Episode", List["Episode"]]] = None
    episodes: Optional[Union["Episode", List["Episode"]]] = None
    numberOfEpisodes: Optional[Union[int, List[int]]] = None
    partOfSeries: Optional[Union["CreativeWorkSeries", List["CreativeWorkSeries"]]] = (
        None
    )
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    seasonNumber: Optional[Union[int, List[int], str, List[str]]] = None
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
