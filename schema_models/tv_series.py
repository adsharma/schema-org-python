from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.creative_work_season import CreativeWorkSeason
from schema_models.episode import Episode
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class TVSeries(CreativeWork):
    """
    CreativeWorkSeries dedicated to TV broadcast and associated online delivery.
    """

    actor: Optional[
        Union["PerformingGroup", List["PerformingGroup"], Person, List[Person]]
    ] = None
    actors: Optional[Union[Person, List[Person]]] = None
    containsSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    episode: Optional[Union[Episode, List[Episode]]] = None
    episodes: Optional[Union[Episode, List[Episode]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = (
        None
    )
    numberOfEpisodes: Optional[Union[int, List[int]]] = None
    numberOfSeasons: Optional[Union[int, List[int]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    season: Optional[
        Union[CreativeWorkSeason, List[CreativeWorkSeason], HttpUrl, List[HttpUrl]]
    ] = None
    seasons: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
