from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.creative_work_season import CreativeWorkSeason
from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.episode import Episode
from schema_models.game_play_mode import GamePlayMode
from schema_models.integer import Integer
from schema_models.music_group import MusicGroup
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.place import Place
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL
from schema_models.video_object import VideoObject


class VideoGameSeries(CreativeWorkSeries):
    numberOfSeasons: Optional[Union[Integer, List[Integer]]] = None
    gameLocation: Optional[Union[URL, List[URL]]] = None
    gameLocation: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    gameLocation: Optional[Union[Place, List[Place]]] = None
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = None
    numberOfPlayers: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfEpisodes: Optional[Union[Integer, List[Integer]]] = None
    seasons: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    season: Optional[Union[URL, List[URL]]] = None
    season: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    gameItem: Optional[Union[Thing, List[Thing]]] = None
    cheatCode: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    characterAttribute: Optional[Union[Thing, List[Thing]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    episode: Optional[Union[Episode, List[Episode]]] = None
    gamePlatform: Optional[Union[Thing, List[Thing]]] = None
    gamePlatform: Optional[Union[Text, List[Text]]] = None
    gamePlatform: Optional[Union[URL, List[URL]]] = None
    playMode: Optional[Union[GamePlayMode, List[GamePlayMode]]] = None
    episodes: Optional[Union[Episode, List[Episode]]] = None
    containsSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    quest: Optional[Union[Thing, List[Thing]]] = None
