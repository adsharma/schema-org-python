from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class TVSeries(CreativeWork):
    """
    CreativeWorkSeries dedicated to TV broadcast and associated online delivery.
    """

    episodes: Optional[Union["Episode", List["Episode"]]] = None
    containsSeason: Optional[
        Union["CreativeWorkSeason", List["CreativeWorkSeason"]]
    ] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    numberOfSeasons: Optional[Union[int, List[int]]] = None
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
    numberOfEpisodes: Optional[Union[int, List[int]]] = None
    seasons: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    season: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    season: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    titleEIDR: Optional[Union[str, List[str]]] = None
    titleEIDR: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    episode: Optional[Union["Episode", List["Episode"]]] = None
