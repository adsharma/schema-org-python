from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.creative_work_season import CreativeWorkSeason
from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.episode import Episode
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.place import Place
from schema_models.thing import Thing


@dataclass
class VideoGameSeries(CreativeWorkSeries):
    """
    A video game series.
    """

    actor: Optional[
        Union[PerformingGroup, List[PerformingGroup], Person, List[Person]]
    ] = None
    actors: Optional[Union[Person, List[Person]]] = None
    characterAttribute: Optional[Union[Thing, List[Thing]]] = None
    cheatCode: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    containsSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    episode: Optional[Union[Episode, List[Episode]]] = None
    episodes: Optional[Union[Episode, List[Episode]]] = None
    gameItem: Optional[Union[Thing, List[Thing]]] = None
    gameLocation: Optional[
        Union[
            Place,
            List[Place],
            "PostalAddress",
            List["PostalAddress"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    gamePlatform: Optional[
        Union[str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]
    ] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = (
        None
    )
    numberOfEpisodes: Optional[Union[int, List[int]]] = None
    numberOfPlayers: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    numberOfSeasons: Optional[Union[int, List[int]]] = None
    playMode: Optional[Union["GamePlayMode", List["GamePlayMode"]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    quest: Optional[Union[Thing, List[Thing]]] = None
    season: Optional[
        Union[CreativeWorkSeason, List[CreativeWorkSeason], HttpUrl, List[HttpUrl]]
    ] = None
    seasons: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
