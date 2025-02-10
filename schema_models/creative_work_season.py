from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.episode import Episode
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class CreativeWorkSeason(CreativeWork):
    """
    A media season, e.g. TV, radio, video game etc.
    """

    endDate: Optional[Union[date, List[date]]] = None
    endDate: Optional[Union[datetime, List[datetime]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    seasonNumber: Optional[Union[int, List[int]]] = None
    seasonNumber: Optional[Union[str, List[str]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    episode: Optional[Union[Episode, List[Episode]]] = None
    partOfSeries: Optional[Union["CreativeWorkSeries", List["CreativeWorkSeries"]]] = (
        None
    )
    episodes: Optional[Union[Episode, List[Episode]]] = None
    startDate: Optional[Union[datetime, List[datetime]]] = None
    startDate: Optional[Union[date, List[date]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
    numberOfEpisodes: Optional[Union[int, List[int]]] = None
