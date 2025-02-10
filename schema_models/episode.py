from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class Episode(CreativeWork):
    """
    A media episode (e.g. TV, radio, video game) which can be part of a series or season.
    """

    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"]]] = None
    partOfSeason: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = (
        None
    )
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    episodeNumber: Optional[Union[str, List[str]]] = None
    episodeNumber: Optional[Union[int, List[int]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    partOfSeries: Optional[Union["CreativeWorkSeries", List["CreativeWorkSeries"]]] = (
        None
    )
